from xml.etree.ElementTree import Element, SubElement, tostring


class SVGBuilder:
    def __init__(self, width, height):
        self.svg = Element(
            "svg",
            {
                "xmlns": "http://www.w3.org/2000/svg",
                "width": str(width),
                "height": str(height),
                "viewBox": f"0 0 {width} {height}",
            },
        )

    def rect(self, x, y, w, h, fill, rx=0):
        SubElement(
            self.svg,
            "rect",
            {
                "x": str(x),
                "y": str(y),
                "width": str(w),
                "height": str(h),
                "fill": fill,
                "rx": str(rx),
            },
        )

    def outlined_rect(
        self,
        x,
        y,
        w,
        h,
        fill,
        stroke,
        stroke_width=2,
        rx=18,
    ):
        SubElement(
            self.svg,
            "rect",
            {
                "x": str(x),
                "y": str(y),
                "width": str(w),
                "height": str(h),
                "rx": str(rx),
                "fill": fill,
                "stroke": stroke,
                "stroke-width": str(stroke_width),
            },
        )

    def line(self, x1, y1, x2, y2, color, width=1):
        SubElement(
            self.svg,
            "line",
            {
                "x1": str(x1),
                "y1": str(y1),
                "x2": str(x2),
                "y2": str(y2),
                "stroke": color,
                "stroke-width": str(width),
            },
        )

    def circle(self, x, y, r, fill):
        SubElement(
            self.svg,
            "circle",
            {
                "cx": str(x),
                "cy": str(y),
                "r": str(r),
                "fill": fill,
            },
        )

    def text(
        self,
        x,
        y,
        value,
        size=18,
        color="#fff",
        weight="400",
        family="JetBrains Mono, monospace",
    ):
        node = SubElement(
            self.svg,
            "text",
            {
                "x": str(x),
                "y": str(y),
                "fill": color,
                "font-size": str(size),
                "font-family": family,
                "font-weight": weight,
            },
        )

        node.text = value

    def chip(self, x, y, text, bg, color):
        width = len(text) * 10 + 24

        self.rect(
            x,
            y,
            width,
            34,
            bg,
            rx=17,
        )

        self.text(
            x + 12,
            y + 22,
            text,
            15,
            color,
            "600",
        )

        return width

    def save(self, path):
        with open(path, "wb") as f:
            f.write(tostring(self.svg))