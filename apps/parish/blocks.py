from wagtail import blocks


class IconTextBlock(blocks.StructBlock):
    icon = blocks.CharBlock(max_length=40, required=False)
    heading = blocks.CharBlock(max_length=100)
    text = blocks.TextBlock()

    class Meta:
        icon = "doc-full"
