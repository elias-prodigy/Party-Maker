from django_tables2 import tables, TemplateColumn, LinkColumn, Column, CheckBoxColumn

from event.models import PartyRegPartners
from .models import Partners


class PartnerTable(tables.Table):

    T1 = '<button type="button" class="btn btn-primary js-update" data-toggle="modal" data-target="#exampleModal" ' \
         'update_link="{{ record.get_absolute_url_update }}">Update</button>'
    T2 = '<button type="button" class="btn js-delete" ' \
         'delete-link="{{ record.get_absolute_url_delete }}">Delete</button>'
    edit = TemplateColumn(T1)
    delete = TemplateColumn(T2)

    name = Column(attrs={"td": {"class": "name"}})
    surname = Column(attrs={"td": {"class": "surname"}})
    sponsor = Column(attrs={"td": {"class": "sponsor"}})
    manager_name = Column(attrs={"td": {"class": "manager_name"}})

    class Meta:
        model = Partners
        fields = ['name', 'surname', 'email', 'sponsor', 'manager_name']


class EventPartnerTable(tables.Table):

    T1 = '<button type="button" class="btn btn-primary js-update" data-toggle="modal" data-target="#exampleModal" ' \
         'update_link="{{ record.get_absolute_url_update }}">Update</button>'
    T2 = '<button type="button" class="btn js-delete" ' \
         'delete-link="{{ record.get_absolute_url_delete }}">Delete</button>'
    edit = TemplateColumn(T1)
    delete = TemplateColumn(T2)

    name = Column(attrs={"td": {"class": "name"}})
    surname = Column(attrs={"td": {"class": "surname"}})
    sponsor = Column(attrs={"td": {"class": "sponsor"}})
    manager_name = Column(attrs={"td": {"class": "manager_name"}})
    manager_approve = TemplateColumn('<input type="checkbox" name="manager_approve" />', attrs={"td": {"class": "manager_approve"}})
    CEO_approve = TemplateColumn('<input type="checkbox" name="CEO_approve" />', attrs={"td": {"class": "CEO_approve"}})

    class Meta:
        model = PartyRegPartners
        fields = ['name', 'surname', 'email', 'sponsor', 'manager_name', 'manager_approve', 'CEO_approve']