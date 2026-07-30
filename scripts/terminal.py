def draw_terminal(builder, cfg, theme):

    width = cfg["layout"]["width"]
    header = cfg["layout"]["header_height"]

    builder.rect(
        0,
        0,
        width,
        header,
        theme["border"],
    )

    builder.text(
        30,
        32,
        cfg["terminal"]["title"],
        18,
        theme["text"],
        "700",
    )

    builder.text(
        width - 100,
        32,
        cfg["terminal"]["live_text"],
        16,
        theme["success"],
    )

    builder.line(
        0,
        header,
        width,
        header,
        theme["primary"],
    )