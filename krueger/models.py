from django.db import models
from customers.models import Customer
#from inventory.models import Inventory

class MiscCost(models.Model):
    description = models.CharField('description', max_length=100, blank=False, null=False)
    price = models.DecimalField('price each', blank=True, null=True, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.description

class PaperStock(models.Model):
    description = models.CharField('description', max_length=100, blank=False, null=False)
    manufacturer = models.CharField('manufacturer', max_length=100, blank=True, null=True)
    brand = models.CharField('brand', max_length=100, blank=True, null=True)
    weight = models.CharField('weight', max_length=100, blank=False, null=False)
    size = models.CharField('size', max_length=100, blank=False, null=False)
    price_per_m = models.CharField('Paper Stock Price per M', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.manufacturer


class KruegerJobDetail(models.Model):
    class JobQuote(models.TextChoices):
        WORKORDER = "Workorder"
        QUOTE = "Quote"

    class Company(models.TextChoices):
        LK = "LK"
        KRUEGER = "KRUEGER"

    jobnumber = models.CharField('Job Number', max_length=100, blank=True, null=True)
    jobquote = models.CharField('Workorder or Quote', max_length=100, choices=JobQuote.choices, blank=False, null=False)
    company = models.CharField('Company', max_length=100, choices=Company.choices, blank=False, null=False)
    customer = models.ForeignKey(Customer, blank=False, null=False, on_delete=models.SET_DEFAULT, default=2)
    description = models.CharField('Job Description', max_length=100, blank=False, null=False)
    set_per_book = models.PositiveIntegerField('# of sets / books/ pieces', blank=True, null=True)
    pages_per_book = models.PositiveBigIntegerField('Pages per Book', blank=True, null=True)
    qty_of_sheets = models.CharField('Qty of Sheets', max_length=10, blank=True, null=True)
    original_size = models.CharField('Original Size', max_length=100, blank=True, null=True)
    press_size = models.CharField('Press Size', max_length=100, blank=True, null=True)
    press_size_per_parent = models.CharField('Press sheets / Parent', max_length=100, blank=True, null=True)
    flat_size = models.CharField('Flat Size', max_length=100, blank=True, null=True)
    finished_size = models.CharField('Finished Size', max_length=100, blank=True, null=True)
    gangup = models.PositiveBigIntegerField('Gangup', blank=True, null=True)
    overage = models.PositiveBigIntegerField('Overage', blank=True, null=True)
    output_per_sheet = models.CharField('Output per Parent Sheet', max_length=10, blank=True, null=True)
    parent_sheets_required = models.CharField('Parent Sheets Required', max_length=10, blank=True, null=True)
    side_1_clicks = models.CharField('Side 1 Clicks', max_length=100, blank=True, null=True)
    side_2_clicks = models.CharField('Side 2 Clicks', max_length=100, blank=True, null=True)
    #stock_paperstock = models.ForeignKey(Inventory, blank=False, null=True, on_delete=models.DO_NOTHING)
    #paper_stock = models.CharField('Paper Stock', max_length=100, blank=True, null=True)
    paper_stock = models.ForeignKey(PaperStock, blank=True, null=True, on_delete=models.DO_NOTHING)
    price_per_m = models.CharField('Paper Stock Price per M', max_length=100, blank=True, null=True)
    #step_workorder = models.CharField('Create Workorder', max_length=12, blank=True, null=True)
    step_workorder_price = models.CharField('Create Workorder', max_length=12, blank=True, null=True)
    #step_reclaim_artwork = models.CharField('Reclaim Artwork', max_length=12, blank=True, null=True)
    step_reclaim_artwork_price = models.CharField('Reclaim Artwork', max_length=12, blank=True, null=True)
    #step_send_to_press = models.CharField('Send to Press', max_length=12, blank=True, null=True)
    step_send_to_press_price = models.CharField('Send to Press', max_length=12, blank=True, null=True)
    #step_send_mailmerge_to_press = models.CharField('Send Mailmerge to press', max_length=12, blank=True, null=True)
    step_send_mailmerge_to_press_price = models.CharField('Send Mailmerge to press', max_length=12, blank=True, null=True)
    #step_print_mailmerge = models.CharField('Print Mailmerge', max_length=12, blank=True, null=True)
    mailmerge_qty = models.CharField('Mailmerge Qty', max_length=12, blank=True, null=True)
    mailmerge_price_per_piece = models.CharField('Mailmerge Price/Piece', max_length=12, blank=True, null=True)
    step_print_mailmerge_price = models.CharField('Mailmerge', max_length=12, blank=True, null=True)
    material_cost = models.CharField('Material Cost', max_length=12, blank=True, null=True)
    material_markup_percentage = models.CharField('Material Markup Percent', max_length=12, blank=True, null=True)
    material_markup = models.CharField('Material Markup Amount', max_length=12, blank=True, null=True)
    #step_wear_and_tear = models.CharField('Wear and Tear', max_length=12, blank=True, null=True)
    step_wear_and_tear_price = models.CharField('Wear and Tear', max_length=12, blank=True, null=True)
    #step_print_side_1 = models.CharField('Print Side 1', max_length=12, blank=True, null=True)
    step_print_cost_side_1 = models.CharField('Side 1 Price / Click', max_length=12, blank=True, null=True)
    step_print_cost_side_1_price = models.CharField('Print Cost Side 1', max_length=12, blank=True, null=True)
    #step_print_side_2 = models.CharField('Print Side 2', max_length=12, blank=True, null=True)
    step_print_cost_side_2 = models.CharField('Side 2 Price / Click', max_length=12, blank=True, null=True)
    step_print_cost_side_2_price = models.CharField('Printing Cost Side 1', max_length=12, blank=True, null=True)
    #step_trim_to_size = models.CharField('Trim to Size', max_length=12, blank=True, null=True)
    step_trim_to_size_price = models.CharField('Trim to Size', max_length=12, blank=True, null=True)
    #step_NCR_compound = models.CharField('NCR Compound', max_length=12, blank=True, null=True)
    step_NCR_compound_price = models.CharField('NCR Compound', max_length=12, blank=True, null=True)
    #step_white_compound = models.CharField('White Compound', max_length=12, blank=True, null=True)
    step_white_compound_price = models.CharField('White Compound', max_length=12, blank=True, null=True)
    #step_set_to_perf = models.CharField('Set to Perf', max_length=12, blank=True, null=True)
    step_set_to_perf_price = models.CharField('Set to Perf', max_length=12, blank=True, null=True)
    #step_perf = models.CharField('Perf', max_length=12, blank=True, null=True)
    perf_price_per_piece = models.CharField('Price per Piece to Perf', max_length=12, blank=True, null=True)
    perf_number_of_pieces = models.CharField('Pieces to Perf', max_length=12, blank=True, null=True)
    step_perf_price = models.CharField('Cost to Perf', max_length=12, blank=True, null=True)
    #step_set_to_number = models.CharField('Set to Number', max_length=12, blank=True, null=True)
    step_set_to_number_price = models.CharField('Set to Number', max_length=12, blank=True, null=True)
    #step_number = models.CharField('Number', max_length=12, blank=True, null=True)
    number_price_to_number = models.CharField('Price / Piece to Number', max_length=12, blank=True, null=True)
    number_number_of_pieces = models.CharField('Pieces to Number', max_length=12, blank=True, null=True)
    step_number_price = models.CharField('Cost to Number', max_length=12, blank=True, null=True)
    #step_insert_frontback_cover = models.CharField('Insert Front / Back Cover', max_length=12, blank=True, null=True)
    step_insert_frontback_cover_price = models.CharField('Insert Front / Back Cover', max_length=12, blank=True, null=True)
    #step_set_to_drill = models.CharField('Set to Drill', max_length=12, blank=True, null=True)
    step_set_to_drill_price = models.CharField('Set to Drill', max_length=12, blank=True, null=True)
    step_drill_price = models.CharField('Drill', max_length=12, blank=True, null=True)
    #step_set_to_staple = models.CharField('Set to Staple', max_length=12, blank=True, null=True)
    step_set_to_staple_price = models.CharField('Set to Staple', max_length=12, blank=True, null=True)
    #step_staple = models.CharField('Staple', max_length=12, blank=True, null=True)
    staple_price_per_staple = models.CharField('Price per staple', max_length=12, blank=True, null=True)
    staple_staples_per_piece = models.CharField('Staples per piece', max_length=12, blank=True, null=True)
    staple_number_of_pieces = models.CharField('Number of pieces', max_length=12, blank=True, null=True)
    step_staple_price = models.CharField('Cost to Staple', max_length=12, blank=True, null=True)
    #step_insert_wrap_around = models.CharField('Insert Wrap Around', max_length=12, blank=True, null=True)
    step_insert_wrap_around_price = models.CharField('Insert Wrap Around', max_length=12, blank=True, null=True)
    #step_insert_chip_divider = models.CharField('Insert Chip Divider', max_length=12, blank=True, null=True)
    step_insert_chip_divider_price = models.CharField('Insert Chip Divider', max_length=12, blank=True, null=True)
    #step_set_folder = models.CharField('Set Folder', max_length=12, blank=True, null=True)
    step_set_folder_price = models.CharField('Set Folder', max_length=12, blank=True, null=True)
    #step_fold = models.CharField('Fold', max_length=12, blank=True, null=True)
    fold_price_per_fold = models.CharField('Price / Fold', max_length=12, blank=True, null=True)
    fold_number_to_fold = models.CharField('Pieces to Fold', max_length=12, blank=True, null=True)
    step_fold_price = models.CharField('Cost to Fold', max_length=12, blank=True, null=True)
    #step_tab_for_mailing = models.CharField('Tab for Mailing', max_length=12, blank=True, null=True)
    tabs_price_per_tab = models.CharField('Price / Tab', max_length=12, blank=True, null=True)
    tabs_per_piece = models.CharField('Tabs / Piece', max_length=12, blank=True, null=True)
    tabs_number_of_pieces = models.CharField('Number of Pieces', max_length=12, blank=True, null=True)
    step_tab_price = models.CharField('Cost to Tab for Mailing', max_length=12, blank=True, null=True)
    misc1_description = models.CharField('Misc extra 1 description', max_length=50, blank=True, null=True)
    misc1_price = models.CharField('Misc extra 1 price', max_length=50, blank=True, null=True)
    misc2_description = models.CharField('Misc extra 2 description', max_length=50, blank=True, null=True)
    misc2_price = models.CharField('Misc extra 2 price', max_length=50, blank=True, null=True)
    misc3_description = models.CharField('Misc extra 3 description', max_length=50, blank=True, null=True)
    misc3_price = models.CharField('Misc extra 3 price', max_length=50, blank=True, null=True)
    misc4_description = models.CharField('Misc extra 4 description', max_length=50, blank=True, null=True)
    misc4_price = models.CharField('Misc extra 4 price', max_length=50, blank=True, null=True)
    #step_bulk_mail_tray_sort_paperwork = models.CharField('Prepare Bulk Mailing', max_length=12, blank=True, null=True)
    step_bulk_mail_tray_sort_paperwork_price = models.CharField('Prepare Bulk Mailing', max_length=12, blank=True, null=True)
    #step_id_count = models.CharField('ID / Count', max_length=12, blank=True, null=True)
    step_id_count_price = models.CharField('ID / Count', max_length=12, blank=True, null=True)
    #step_count_package = models.CharField('Count / Package', max_length=12, blank=True, null=True)
    step_count_package_price = models.CharField('Count / Package', max_length=12, blank=True, null=True)
    #step_delivery = models.CharField('Delivery', max_length=12, blank=True, null=True)
    step_delivery_price = models.CharField('Delivery', max_length=12, blank=True, null=True)
    #step_packing_slip = models.CharField('Packing Slip', max_length=12, blank=True, null=True)
    step_packing_slip_price = models.CharField('Packing Slip', max_length=12, blank=True, null=True)
    price_total = models.CharField('Total Price', max_length=10, blank=True, null=True)
    price_total_per_m =models.CharField('Price / M', max_length=10, blank=True, null=True)
    dateentered = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.company + ' ' + self.description


