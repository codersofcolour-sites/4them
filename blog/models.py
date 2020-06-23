from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.embeds.blocks import EmbedBlock

from streams import blocks as my_blocks

class BlogIndexPage(Page):
    """Blog Index Page"""
    template = "blog/blog_index_page.html"     

    intro = RichTextField(blank=True)
    content = StreamField(
        [
            ("title_and_text", my_blocks.TitleAndTextBlock()),
            ("cards", my_blocks.CardBlock()),
            ('embed', EmbedBlock(icon="media")),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]
    def get_context(self, request):
        # Update context to include only published posts, 
        # in reverse chronological order
        context = super(BlogIndexPage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        return context
    

class BlogPage(Page):
    template = "blog/blog_page.html"
    date = models.DateField("Post date")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    intro = models.CharField(max_length=250)
    body = StreamField([
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('embed', EmbedBlock(icon="media")),
])
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('intro'),
        StreamFieldPanel('body', classname="full"),
    ]
