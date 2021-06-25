"""BookingCreate ViewSet"""

from api.serializers.bookingSerializer import BookingSerializer
from api.models.booking import Booking
from api.models.appuser import AppUser
from api.models.container import Container
from api.models.cntrstatus import CntrStatus
from api.models.bkgstatus import BkgStatus
from api.models.due import Due
from api.models.document import Document
from api.models.port import Port
from api.models.carrier import Carrier
from api.models.product import Product
from api.models.voyage import Voyage
from api.models.vessel import Vessel
from api.models.service import Service
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db.models.functions import Lower
from django.http import HttpResponseServerError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import random
import string


class BookingCreateViewSet(ViewSet):
    """
        View module for handling requests about BookingCreates.
        ViewSet handles GET, POST, PUT, DELETE requests sent from client
        over HTTP protocol.

        BookingCreate ViewSet
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """
            Handle GET requests to get all categories resources.
            Returns:
                Response : JSON serialized list of BookingCreate types.
        """

        user = AppUser.objects.get(user=request.auth.user)

        service = request.data['service']
        vessel = request.data['vessel']
        voyage = request.data['voyage']
        carrier = request.data['carrier']
        equipment_type = request.data['equipment_type']
        cntr = request.data['cntr']
        loding_port = request.data['loading_port']
        unloading_port = request.data['unloading_port']
        bkg_status = request.data['status']  # booking
        documents = request.data['documents']
        dues = request.data["dues"]
        issues = request.data['issues']
        pickup = request.data['pickup']
        port_cut = request.data['port_cut']
        rail_cut = request.data['rail_cut']
        address = request.data['address']
        bkg_notes = request.data['bkg_notes']
        cntr_notes = request.data['cntr_notes']
        cntrDamaged = request.data['cntrDamaged']
        inspection = request.data['inspection']
        overweight = request.data['overweight']
        commodity = request.data['commodity']
        weight = request.data['weight']
        fragile = request.data['fragile']
        hazardous = request.data['hazardous']
        reefer = request.data['reefer']
        productDamaged = request.data['productDamaged']

        loading_port_instance = Port.objects.create(
            name=loding_port, location=loding_port, code="UTEST")

        new_service = Service.objects.create(name=service)
        new_vessel = Vessel.objects.create(
            name=vessel, longitude=1.0, latitude=1.0, service=new_service)
        new_voyage = Voyage.objects.create(voyage=voyage, vessel=new_vessel)

        new_carrier = Carrier.objects.create(name=carrier)
        new_document = Document.objects.create(are_docs_ready=documents)
        new_due = Due.objects.create(are_dues_paid=dues)
        new_bkg_status = BkgStatus.objects.create(status=bkg_status)

        # fix on frontend
        new_cntr_status = CntrStatus.objects.create(status="Yard")

        new_container = Container.objects.create(
            container=cntr,
            equipment_size=equipment_type,
            container_status=new_cntr_status,
            is_damaged=cntrDamaged,
            is_need_inspection=inspection,
            is_overweight=overweight,
            is_in_use=False,
            notes=cntr_notes)

        new_product = Product.objects.create(
            commodity=commodity,
            weight=weight,
            is_fragile=fragile,
            is_haz=hazardous,
            is_damaged=productDamaged,
            is_reefer=reefer,
            container=new_container)

        new_booking = Booking.objects.create(
            user=user,
            booking=''.join(random.choices(
                string.ascii_uppercase + string.digits, k=10)),
            voyage_reference=new_voyage,
            container=new_container,
            carrier=new_carrier,
            loading_origin=loading_port_instance.name,
            unloading_destination=unloading_port,
            pickup_address=address,
            pickup_appt=pickup,
            port=loading_port_instance,
            port_cutoff=port_cut,
            rail_cutoff=rail_cut,
            document=new_document,
            due=new_due,
            has_issue=issues,
            booking_status=new_bkg_status,
            notes=bkg_notes)

        try:

            new_booking.save()
            serializer = BookingSerializer(
                new_booking, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
