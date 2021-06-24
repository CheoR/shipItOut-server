"""Booking ViewSet"""

from api.models.due import Due
from api.models.document import Document
from api.models.port import Port
from api.models.cntrstatus import CntrStatus
from api.models.container import Container
from api.models.service import Service
from api.models.vessel import Vessel
from api.models.voyage import Voyage
from api.models.bkgstatus import BkgStatus
from api.models.carrier import Carrier
from api.models.appuser import AppUser
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError

from api.models import Booking
from api.serializers import BookingSerializer


class BookingViewSet(ViewSet):
    """
        View module for handling requests about bookings.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        Booking ViewSet
    """

    def list(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Booking types.
        """

        user = AppUser.objects.get(user=request.auth.user)
        bookings = Booking.objects.filter(user=user)

        try:
            # serialzied_bookings = BookingSerializer(
            #     bookings,
            #     many=True,
            #     context=({'request': request})
            # )

            bkg_list = []
            for bkg in bookings:

                booking = Booking.objects.get(user=user, pk=bkg.id)
                carrier = Carrier.objects.get(id=booking.carrier.id)
                status = BkgStatus.objects.get(id=booking.booking_status.id)
                voyage = Voyage.objects.get(id=booking.voyage_reference.id)
                vessel = Vessel.objects.get(id=voyage.vessel.id)
                service = Service.objects.get(id=vessel.service_id)
                container = Container.objects.get(id=booking.container.id)
                cntr_status = CntrStatus.objects.get(
                    id=container.container_status.id)
                port = Port.objects.get(id=booking.port.id)
                document = Document.objects.get(id=booking.document.id)
                money = Due.objects.get(id=booking.due.id)

                data = {}

                data['id'] = booking.id
                data['username'] = request.auth.user.username
                data['full_name'] = F"{request.auth.user.first_name} {request.auth.user.last_name}"
                data['booking_status'] = status.status
                data['booking'] = booking.booking
                data['origin'] = booking.loading_origin
                data['destination'] = booking.unloading_destination
                data['pickup_appt'] = booking.pickup_appt
                data['service'] = service.name
                data['voyage'] = voyage.voyage
                data['vessel'] = vessel.name
                data['longitude'] = vessel.longitude
                data['latitude'] = vessel.latitude
                data['carrier'] = carrier.name
                data['container_status'] = cntr_status.status
                data['container'] = container.container
                data['size'] = container.equipment_size
                data['damaged'] = container.is_damaged
                data['overweight'] = container.is_overweight
                data['needs_inspection'] = container.is_need_inspection
                data['container_available'] = container.is_in_use
                data['port'] = port.code
                data['port_name'] = port.name
                data['port_location'] = port.location
                data['port_cutoff'] = booking.port_cutoff
                data['rail_cutoff'] = booking.rail_cutoff
                data['document_submitted'] = document.are_docs_ready
                data['money_owed'] = money.are_dues_paid
                data['issues'] = booking.has_issue
                data['booking_notes'] = booking.notes
                data['container_notes'] = container.notes

                bkg_list.append(data)

            return Response(bkg_list)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of Booking types.
        """

        user = AppUser.objects.get(user=request.auth.user)

        try:
            booking = Booking.objects.get(user=user, pk=pk)
            # carrier = Carrier.objects.get(id=booking.carrier.id)
            # status = BkgStatus.objects.get(id=booking.booking_status.id)
            # voyage = Voyage.objects.get(id=booking.voyage_reference.id)
            # vessel = Vessel.objects.get(id=voyage.vessel.id)
            # service = Service.objects.get(id=vessel.service_id)
            # container = Container.objects.get(id=booking.container.id)
            # cntr_status = CntrStatus.objects.get(
            #     id=container.container_status.id)
            # port = Port.objects.get(id=booking.port.id)
            # document = Document.objects.get(id=booking.document.id)
            # money = Due.objects.get(id=booking.due.id)

            # data = {}

            # data['id'] = booking.id
            # data['username'] = request.auth.user.username
            # data['full_name'] = F"{request.auth.user.first_name} {request.auth.user.last_name}"
            # data['booking_status'] = status.status
            # data['booking'] = booking.booking
            # data['service'] = service.name
            # data['voyage'] = voyage.voyage
            # data['vessel'] = vessel.name
            # data['longitude'] = vessel.longitude
            # data['latitude'] = vessel.latitude
            # data['carrier'] = carrier.name
            # data['container'] = container.container
            # data['container_status'] = cntr_status.status
            # data['size'] = container.equipment_size
            # data['damaged'] = container.is_damaged
            # data['needs_inspection'] = container.is_need_inspection
            # data['overweight'] = container.is_overweight
            # data['container_notes'] = container.notes
            # data['container_available'] = container.is_in_use
            # data['origin'] = booking.loading_origin
            # data['destination'] = booking.unloading_destination
            # data['pickup_appt'] = booking.pickup_appt
            # data['port'] = port.code
            # data['port_name'] = port.name
            # data['port_location'] = port.location
            # data['port_cutoff'] = booking.port_cutoff
            # data['rail_cutoff'] = booking.rail_cutoff
            # data['document_submitted'] = document.are_docs_ready
            # data['money_owed'] = money.are_dues_paid
            # data['issues'] = booking.has_issue
            # data['booking_notes'] = booking.notes

            serialzied_bookings = BookingSerializer(
                booking,
                context=({'request': request})
            )

            return Response(serialzied_bookings.data)
        except Booking.DoesNotExist as ex:
            return Resposnse({'message': 'The requested order does not exist, or you do not have permission to access it.'},
                             status=status.HTTP_404_NOT_FOUND
                             )
        except Exception as ex:
            return HttpResponseServerError(ex)
