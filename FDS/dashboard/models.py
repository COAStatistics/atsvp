from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Year(models.Model):
    id = models.AutoField(primary_key=True)
    Year = models.IntegerField(_("Year"))

    def __str__(self):
        return str(self.Year)
    
    def get_model_fields(model):
        return model._meta.fields

    class Meta:
        verbose_name = _("Year")
        verbose_name_plural = _("Year")
        ordering = ['Year']

class SectorName(models.Model):
    Name = models.CharField(max_length=100, verbose_name=_("Sector"))

    def __str__(self):
        return self.Name
    
    def get_model_fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        verbose_name = _("Sector")
        verbose_name_plural = _("Sector")

class StageShare(models.Model):
    FarmGate = models.FloatField(verbose_name=_("Farm Gate"), default=0)
    TransGate = models.FloatField(verbose_name=_("Trans Gate"), default=0)
    ProcessGate = models.FloatField(verbose_name=_("Process Gate"), default=0)
    TradeGate = models.FloatField(verbose_name=_("Trade Gate"), default=0)

    Sector = models.ForeignKey(
        SectorName, on_delete=models.CASCADE, verbose_name=_("Sector")
    )
    Year = models.ForeignKey(
        Year, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Year")
    )

    def __str__(self):
        return 'Sector: %s, Year: %s, FarmGate: %s, TransGate: %s, ProcessGate: %s, TradeGate: %s' % (
            self.Sector.Name, self.Year.Year, self.FarmGate, self.TransGate, self.ProcessGate, self.TradeGate
        )
    
    def __unicode__(self):
        return 'Sector: %s, Year: %s, FarmGate: %s, TransGate: %s, ProcessGate: %s, TradeGate: %s' % (
            self.Sector.Name, self.Year.Year, self.FarmGate, self.TransGate, self.ProcessGate, self.TradeGate
        )

    def get_model_fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        verbose_name = _("Stage Share")
        verbose_name_plural = _("Stage Share")
        ordering = ['Year']

class Marketing(models.Model):
    FarmShare = models.FloatField(verbose_name=_("Farm Share"), default=0)
    MarketingShare = models.FloatField(verbose_name=_("Marketing Share"), default=0)
    Sector = models.ForeignKey(
        SectorName, on_delete=models.CASCADE, verbose_name=_("Sector")
    )
    Year = models.ForeignKey(
        Year, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Year")
    )

    def __str__(self):
        return '%s, Farm Share: %s,Marketing Share: %s' % (
            self.Sector.Name, self.FarmShare, self.MarketingShare
        )

    def __unicode__(self):
        return '%s, Farm Share: %s,Marketing Share: %s' % (
            self.Sector.Name, self.FarmShare, self.MarketingShare
        )

    class Meta:
        verbose_name = _("Marketing Bill")
        verbose_name_plural = _("Marketing Bill")
        ordering = ['Year']

class Industry(models.Model):
    Agribusiness = models.FloatField(verbose_name=_('Agribusiness'), default=0)
    FarmProduction = models.FloatField(verbose_name=_('Farm Production'), default=0)
    FoodProcess = models.FloatField(verbose_name=_('Food Process'), default=0)
    Packaging = models.FloatField(verbose_name=_('Packaging'), default=0)
    Transportation = models.FloatField(verbose_name=_('Transportation'), default=0)
    WholesaleTrade = models.FloatField(verbose_name=_('Wholesale trade'), default=0)
    RetailTrade = models.FloatField(verbose_name=_('Retail trade'), default=0)
    Trade = models.FloatField(verbose_name=_('Trade'), default=0)
    FoodService = models.FloatField(verbose_name=_('Food service'), default=0)
    Energy = models.FloatField(verbose_name=_('Energy'), default=0)
    FinanceInsurance = models.FloatField(verbose_name=_('Finance and insurance'), default=0)
    Advertising = models.FloatField(verbose_name=_('Advertising'), default=0)
    Accounting = models.FloatField(verbose_name=_('Accounting'), default=0)
    Sector = models.ForeignKey(
        SectorName, on_delete=models.CASCADE, verbose_name=_("Sector")
    )
    Year = models.ForeignKey(
        Year, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Year")
    )

    def __str__(self):
        return '%s, Agribusiness: %s, Farm Production: %s, Food Process: %s, Packaging: %s, Transportation: %s, Wholesale trade: %s, Retail trade: %s, Trade: %s, Food service: %s, Energy: %s, Finance and insurance: %s, Advertising: %s' % (
            self.Sector.Name, self.Agribusiness, self.FarmProduction, self.FoodProcess, self.Packaging, self.Transportation, self.WholesaleTrade, self.RetailTrade, self.Trade, self.FoodService, self.Energy, self.FinanceInsurance, self.Advertising
        )

    def __unicode__(self):
        return '%s, Agribusiness: %s, Farm Production: %s, Food Process: %s, Packaging: %s, Transportation: %s, Wholesale trade: %s, Retail trade: %s, Trade: %s, Food service: %s, Energy: %s, Finance and insurance: %s, Advertising: %s' % (
            self.Sector.Name, self.Agribusiness, self.FarmProduction, self.FoodProcess, self.Packaging, self.Transportation, self.WholesaleTrade, self.RetailTrade, self.Trade, self.FoodService, self.Energy, self.FinanceInsurance, self.Advertising
        )

    def get_model_fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]
    
    class Meta:
        verbose_name = _("Industry Group")
        verbose_name_plural = _("Industry Group")
        ordering = ['Year']

class Primary(models.Model):
    Compensation = models.FloatField(verbose_name=_('Compensation'), default=0)
    OperatingSurplus = models.FloatField(verbose_name=_('Operating Surplus'), default=0)
    ConsumptionOfFixedCapital = models.FloatField(verbose_name=_('Consumption of Fixed Capital'), default=0)
    NetTaxes = models.FloatField(verbose_name=_('Net taxes'), default=0)
    Adjustment = models.FloatField(verbose_name=_('Adjustment'), default=0)
    Imports = models.FloatField(verbose_name=_('Imports'), default=0)

    Sector = models.ForeignKey(
        SectorName, on_delete=models.CASCADE, verbose_name=_('Sector')
    )
    Year = models.ForeignKey(
        Year, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Year")
    )

    def __str__(self):
        return 'Sector: %s, Compensation: %s, Operating Surplus: %s, Consumption of Fixed Capital: %s, Net taxes: %s, Adjustment: %s, Imports: %s' % (
            self.Sector.Name, self.Compensation, self.OperatingSurplus, self.ConsumptionOfFixedCapital, self.NetTaxes, self.Adjustment, self.Imports
        )
    
    def __unicode__(self):
        return 'Sector: %s, Compensation: %s, Operating Surplus: %s, Consumption of Fixed Capital: %s, Net taxes: %s, Adjustment: %s, Imports: %s' % (
            self.Sector.Name, self.Compensation, self.OperatingSurplus, self.ConsumptionOfFixedCapital, self.NetTaxes, self.Adjustment, self.Imports
        )
    
    def get_model_fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]
    
    class Meta:
        verbose_name = _("Primary Factor")
        verbose_name_plural = _("Primary Factor")
        ordering = ['Year']

class IndustryCrossPrimary(models.Model):
    Industry = models.CharField(max_length=100, verbose_name=_('Name'), null=True, blank=True, default='')
    Compensation = models.FloatField(verbose_name=_('Compensation')+"%")
    OperatingSurplus = models.FloatField(verbose_name=_('Operating Surplus')+"%")
    ConsumptionOfFixedCapital = models.FloatField(verbose_name=_('Consumption of Fixed Capital')+"%")
    NetTaxes = models.FloatField(verbose_name=_('Net taxes')+"%")
    Imports = models.FloatField(verbose_name=_('Imports')+"%")
    Total = models.FloatField(verbose_name=_('Total')+"%")

    def __str__(self):
        return 'Industry: %s, Compensation: %s, Operating Surplus: %s, Consumption of Fixed Capital: %s, Net taxes: %s, Imports: %s, Total: %s' % (
            self.Industry ,self.Compensation, self.OperatingSurplus, self.ConsumptionOfFixedCapital, self.NetTaxes, self.Imports, self.Total
        )
    
    def __unicode__(self):
        return 'Industry: %s, Compensation: %s, Operating Surplus: %s, Consumption of Fixed Capital: %s, Net taxes: %s, Imports: %s, Total: %s' % (
            self.Industry ,self.Compensation, self.OperatingSurplus, self.ConsumptionOfFixedCapital, self.NetTaxes, self.Imports, self.Total
        )
    
    class Meta:
        verbose_name = _("Primary & industry cross-tablated statistics")
        verbose_name_plural = _("Primary & industry cross-tablated statistics")