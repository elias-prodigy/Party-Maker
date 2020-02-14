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


class CheckBoxColumnWithName(CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class EventPartnerTable(tables.Table):

    T3 = '<button type="button" class="btn btn-primary partner-event-update" data-toggle="modal" data-target="#PartnersOnEvent" ' \
         'update_partner_on_event_link="{{ record.get_absolute_url_update_partner }}">Update</button>'
    T4 = '<button type="button" class="btn js-delete" ' \
         'delete-link="{{ record.partner.get_absolute_url_delete }}">Delete</button>'
    edit = TemplateColumn(T3)
    delete = TemplateColumn(T4)

    name = Column(attrs={"td": {"class": "modal_name"}}, accessor="partner.name")
    surname = Column(attrs={"td": {"class": "modal_surname"}}, accessor="partner.surname")
    sponsor = Column(attrs={"td": {"class": "modal_sponsor"}}, accessor="partner.sponsor")
    email = Column(attrs={"td": {"class": "modal_email"}}, accessor="partner.email")
    manager_name = Column(attrs={"td": {"class": "modal_manager_name"}}, accessor="partner.manager_name")

    manager_approve = CheckBoxColumnWithName(verbose_name="Manager approve", orderable="True")
    CEO_approve = CheckBoxColumnWithName(verbose_name="CEO approve", orderable="True")
    # manager_approve = TemplateColumn('<input type="checkbox" id="{{ record.id }}" value="{{ record.manager_approve }}" />', verbose_name="Manager approve")
    # CEO_approve = TemplateColumn('<input type="checkbox" id="{{ record.id }}" value="{{ record.CEO_approve }}" />', verbose_name="CEO approve")

    class Meta:
        model = PartyRegPartners
        fields = ['event', 'name', 'surname', 'email', 'sponsor', 'manager_name', 'manager_approve', 'CEO_approve']
