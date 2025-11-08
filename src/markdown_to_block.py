def markdown_to_blocks(markdown:str):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        new_subblocks = block.split("\n")
        stripped_block = [b.strip() for b in new_subblocks]
        freshly_baked_stripped_blocks = [b for b in stripped_block if b !=""]
        append_stripped_blocks = "\n".join(freshly_baked_stripped_blocks)
        stripped_blocks.append(append_stripped_blocks)
    final = []
    for stripped in stripped_blocks:
        if stripped == "":
            continue
        final.append(stripped)
    return final