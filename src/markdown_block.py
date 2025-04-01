import enum


class BlockType(enum.Enum):
    PARAGRAPH = 'paragraph'
    HEADER = 'header'
    QUOTE = 'quote'
    CODE = 'code'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def markdown_to_blocks(markdown):
    return [x.strip() for x in markdown.split("\n\n") if x.strip() != ""]


def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith(tuple("#"*i for i in range(1, 7))):
        return BlockType.HEADER

    split = block.split("\n")
    if block.startswith(">"):
        for line in split:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for line in split:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        i = 1
        for line in split:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
