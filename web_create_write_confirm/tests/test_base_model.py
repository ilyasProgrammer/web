from odoo.tests.common import SavepointCase


class TestBaseModel(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestBaseModel, cls).setUpClass()
        cls.base_model = cls.env["base"]

    def test_get_message_information(self):
        self.assertFalse(self.base_model.get_message_information())

    def test_execute_processing(self):
        self.assertTrue(self.base_model.execute_processing())
