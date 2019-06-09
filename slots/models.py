from django.contrib.auth.models import User
from django.db import models, transaction
from django.contrib.gis.db import models as gis_model


class Base(models.Model):
    created_dt = models.DateTimeField(auto_now=True)
    updated_dt = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Slot(Base):

    AVAILABLE = 'available'
    BOOKED = 'booked'
    RESERVED = 'reserved'
    STATUS_CHOICES = (
        (AVAILABLE, 'available'),
        (BOOKED, 'booked')
    )

    HOURLY = 'hour'
    DAY = 'day'

    PARKING_MODE = (
        (HOURLY, 'Hour'),
        (DAY, 'Day'),
    )

    location = gis_model.PointField()

    parking_mode = models.CharField(max_length=11, choices=PARKING_MODE, default=DAY,
                                    help_text='Decides if slot is available by day or hour')

    price = models.DecimalField(null=True, blank=True, default=0.0, max_digits=6, decimal_places=2)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default=AVAILABLE,
                              help_text='Decides if slot is availaible or booked')

    day = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'slots'



class Reservation(Base):
    CREDIT_CARD = 'Credit Card'
    DEBIT_CARD = 'Debit Card'
    PAYMENT_CHOICE = (
        (CREDIT_CARD, 'Credit Card'),
        (DEBIT_CARD , 'Debit Card')
    )

    CREDIT_CARD = 'Credit Card'
    DEBIT_CARD = 'Debit Card'

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    # release slot if booking deleted.
    slot = models.ForeignKey(Slot, on_delete=models.DO_NOTHING)

    price = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)

    payment_status = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True)

    payment_type = models.CharField(max_length=11, choices=PAYMENT_CHOICE,default=CREDIT_CARD)

    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)

    is_cancelled = models.BooleanField(default=False)

    class Meta:
        db_table = 'Reservations'

    @classmethod
    def reservation(cls, data):
        with transaction.atomic():
            slot = Slot.objects.select_for_update().get(id=data.get('slot').id)
            if slot.status == 'booked':
                return
            slot.status = Slot.BOOKED
            slot.save()
        return slot
