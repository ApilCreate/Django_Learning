from rest_framework.test import APITestCase
from rest_framework import status
from .models import Parent


class ParentUpdateDeleteTests(APITestCase):
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Ada",
            last_name="Lovelace",
            address="London",
            student_name="Byron",
        )

    def test_patch_updates_parent(self):
        response = self.client.patch(
            f"/parent/update/{self.parent.pk}/",
            {"address": "Oxford"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.parent.refresh_from_db()
        self.assertEqual(self.parent.address, "Oxford")
        self.assertEqual(self.parent.first_name, "Ada")

    def test_delete_removes_parent(self):
        response = self.client.delete(f"/parent/delete/{self.parent.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Parent.objects.filter(pk=self.parent.pk).exists())
