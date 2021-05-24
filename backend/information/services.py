from information.models import Address


def update_address(pk, **kwargs):
    address = Address.objects.get(uuid=pk)
    address.__dict__.update(kwargs)
    address.full_clean()
    address.save()
    return address
