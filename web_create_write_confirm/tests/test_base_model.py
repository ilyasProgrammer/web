from odoo.tests.common import SavepointCase


class TestBaseModel(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestBaseModel, cls).setUpClass()
        cls.base_model = cls.env["base"]

    def test_get_message_informations(self):
        """Test correct flow of get_message_informations method"""
        ret_value_of_method = self.base_model.get_message_informations()
        check_ret_value = False
        if (ret_value_of_method is False) or isinstance(
            ret_value_of_method, type(self.env["popup.message"])
        ):
            check_ret_value = True
        self.assertTrue(
            check_ret_value,
            msg="Return value must be False or dictionary of popup.message objects",
        )
        self.env["popup.message"]._compute_field_name()

    def test_execute_processing(self):
        """Test correct flow of execute_processing method"""
        self.assertFalse(
            self.base_model.execute_processing(), msg="Return value must be False"
        )
