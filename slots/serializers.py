from rest_framework.serializers import ModelSerializer

from .models import Slot, Reservation

class SlotSerializer(ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

class ReservationSerializer(ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'


    def create(self, validated_data):
        slot  = Reservation.reservation(validated_data)
        if not slot:
            raise Exception('somebody else have booked it already')
        return super(ReservationSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        slot = instance.slot
        slot.status = slot.AVAILABLE
        slot.save()
        return super(ReservationSerializer, self).update(instance,validated_data)

    def to_internal_value(self, data):
        data.update({'user': self.context.get('request').user.id})
        return super(ReservationSerializer, self).to_internal_value(data)
