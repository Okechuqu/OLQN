from wagtail import blocks


class CallToActionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=120)
    text = blocks.TextBlock(required=False)
    link_text = blocks.CharBlock(max_length=40)
    link_url = blocks.URLBlock()

    class Meta:
        icon = "link"
        template = "components/cards/call_to_action.html"
