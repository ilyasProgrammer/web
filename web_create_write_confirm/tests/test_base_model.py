from odoo.tests.common import SavepointCase


class TestBaseModel(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestBaseModel, cls).setUpClass()
        cls.base_model = cls.env["base"]

    def test_get_message_informations(self):
        self.assertFalse(self.base_model.get_message_informations())

    def test_execute_processing(self):
        self.assertFalse(self.base_model.execute_processing())
