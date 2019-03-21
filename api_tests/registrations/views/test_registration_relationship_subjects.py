import pytest

from api.base.settings.defaults import API_BASE
from api_tests.subjects.mixins import SubjectsRelationshipMixin
from osf_tests.factories import (
    RegistrationFactory
)


@pytest.mark.django_db
class TestRegistrationRelationshipSubjects(SubjectsRelationshipMixin):
    @pytest.fixture()
    def resource(self, user_admin_contrib, user_write_contrib, user_read_contrib):
        registration = RegistrationFactory(is_public=False, creator=user_admin_contrib)
        registration.add_contributor(user_write_contrib, permissions=['write', 'read'])
        registration.add_contributor(user_read_contrib, permissions=['read'])
        registration.save()
        return registration

    @pytest.fixture()
    def url(self, resource):
        return '/{}registrations/{}/relationships/subjects/'.format(API_BASE, resource._id)
