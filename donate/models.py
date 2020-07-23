from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks
    
class DonatePageCarouselImages(Orderable):
    """Between 1 and 5 images for the donate page carousel."""

    page = ParentalKey("donate.DonatePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    caption = models.CharField(max_length=100, blank=True, null=True)

    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("caption"),
        ]
        
class DonatePage(Page):
    """Donate page model."""

    template = "donate/donate_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=True)
    banner_subtitle = RichTextField(max_length=100, blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
   )

    content = StreamField([
        ("title_and_text", blocks.TitleAndTextBlock()),
        ("cta", blocks.CTABlock())]
        , null=True, blank=True)
              

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading="Banner Options",
        ),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image")],
            heading="Carousel Images"
        ),
        StreamFieldPanel("content"),
    ]

    

    class Meta:

        verbose_name = "Donate Page"
        verbose_name_plural = "Donate Pages"