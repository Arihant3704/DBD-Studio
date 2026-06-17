import os

def get_header(title, is_dark=False):
    bg_color = "#111827" if is_dark else "#FCFBF9"
    text_color = "#F9FAFB" if is_dark else "#1F2937"
    border_color = "rgba(255,255,255,0.1)" if is_dark else "#E5E7EB"
    return f"""<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Montserrat', sans-serif;
            background-color: #f3f4f6;
            overflow: hidden;
        }}
        .slide-container {{
            width: 1280px;
            height: 720px;
            position: relative;
            background-color: {bg_color};
            color: {text_color};
            display: flex;
            overflow: hidden;
            box-sizing: border-box;
        }}
        .slide-container-padded {{
            padding: 50px 70px 40px 70px;
            flex-direction: column;
            justify-content: space-between;
        }}
        .font-serif {{
            font-family: 'Playfair Display', serif;
        }}
        .font-sans {{
            font-family: 'Montserrat', sans-serif;
        }}
        .accent-color {{
            color: #C5A47E;
        }}
        .accent-bg {{
            background-color: #C5A47E;
        }}
        .accent-border {{
            border-color: #C5A47E;
        }}
        .border-fine {{
            border-color: {border_color};
        }}
        .slide-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-shrink: 0;
            margin-bottom: 15px;
        }}
        .slide-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 0;
        }}
        .slide-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid {border_color};
            padding-top: 15px;
            font-size: 0.8rem;
            color: {'#9CA3AF' if is_dark else '#6B7280'};
            letter-spacing: 0.1em;
            text-transform: uppercase;
            flex-shrink: 0;
        }}
        .accent-line {{
            width: 80px;
            height: 4px;
            background-color: #C5A47E;
            margin-bottom: 12px;
        }}
        .page-num {{
            font-weight: 700;
            color: #C5A47E;
        }}
        
        /* Custom layout sizing to replace Tailwind JIT arbitrary syntax */
        .w-55 {{ width: 55%; }}
        .w-45 {{ width: 45%; }}
        .w-42 {{ width: 42%; }}
        .w-58 {{ width: 58%; }}
        .w-50 {{ width: 50%; }}
        .h-170 {{ height: 170px; }}
        .h-340 {{ height: 340px; }}
        .h-280 {{ height: 280px; }}
        .p-70 {{ padding: 70px; }}
        .p-80 {{ padding: 80px; }}
        .pb-40 {{ padding-bottom: 40px; }}
        .p-50 {{ padding: 50px; }}
        .p-60 {{ padding: 60px; }}
        .text-10 {{ font-size: 10px; }}
        .text-11 {{ font-size: 11px; }}
        .max-w-90 {{ max-width: 90%; }}
    </style>
</head>
"""

def get_footer_element(page_num_str):
    return f"""
<div class="slide-footer">
    <div>Dream Build Design Studio &nbsp;|&nbsp; Company Profile</div>
    <div class="page-num">{page_num_str}</div>
</div>
"""

def main():
    output_dir = "ppt"
    os.makedirs(output_dir, exist_ok=True)

    # ------------------ SLIDE 1: COVER ------------------
    slide1 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("DBD Studio - Company Profile", is_dark=False)}
<body>
<div class="slide-container flex flex-row">
    <!-- Left panel (Content) -->
    <div class="w-55 h-full p-80 pb-40 flex flex-col justify-between relative z-10">
        <div>
            <div class="flex items-center mb-12">
                <img alt="DBD Studio Logo" src="../photo-video/logo.png" style="height: 64px; object-fit: contain;">
            </div>
            <div class="accent-line"></div>
            <h1 class="font-serif text-5xl font-bold leading-tight text-gray-900 mb-6 mt-8">
                Dream Build Design<br>
                <span class="accent-color italic">Studio</span>
            </h1>
            <p class="font-sans text-xl font-light text-gray-600 leading-relaxed max-w-90">
                Transforming Retail & Residential Spaces into Remarkable Experiences
            </p>
        </div>
        <div class="font-sans text-xs tracking-wider text-gray-500 uppercase flex justify-between items-end border-t border-gray-200 pt-6">
            <div>
                <p>Retail & Residential Interior Design &bull; Bangalore</p>
                <p class="mt-2 font-bold accent-color">Company Profile &bull; 2026</p>
            </div>
            <div class="page-num font-bold">01</div>
        </div>
    </div>
    
    <!-- Right panel (Image with gold border) -->
    <div class="w-45 h-full relative overflow-hidden">
        <div class="absolute left-0 top-0 bottom-0 w-2 accent-bg z-20"></div>
        <div class="w-full h-full bg-cover bg-center transition-transform duration-500 hover:scale-105" 
             style="background-image: url('../photo-video/WhatsApp Image 2025-08-11 at 10.51.15 (1).jpeg');">
        </div>
        <div class="absolute inset-0 bg-gray-900 bg-opacity-20"></div>
    </div>
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "1.html"), "w") as f:
        f.write(slide1)

    # ------------------ SLIDE 2: ABOUT FOUNDER ------------------
    slide2 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("About DBD Studio", is_dark=False)}
<body>
<div class="slide-container flex flex-row">
    <!-- Left column -->
    <div class="w-42 h-full bg-gray-100 bg-opacity-60 p-70 pb-40 flex flex-col justify-between border-r border-gray-200 relative">
        <div class="absolute top-0 right-0 w-1 accent-bg h-1/5"></div>
        <div class="my-auto">
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-3">01 / Introduction</span>
            <div class="accent-line"></div>
            <h1 class="font-serif text-4xl font-bold text-gray-900 mb-8 leading-tight">
                About<br>DBD Studio
            </h1>
            <div class="border-t border-gray-300 pt-6 mt-8">
                <p class="font-serif text-xl italic text-gray-800 font-semibold mb-2">Beulah Hephzibah</p>
                <p class="font-sans text-xs tracking-wider text-gray-500 uppercase">Lead Principal / Founder &amp; Visionary</p>
            </div>
            <div class="flex items-center text-gray-500 mt-8">
                <i class="fas fa-map-marker-alt accent-color text-lg mr-3"></i>
                <span class="font-sans text-sm font-medium">Electronic City, Bangalore</span>
            </div>
        </div>
    </div>
    
    <!-- Right column -->
    <div class="w-58 h-full p-70 pb-40 flex flex-col justify-between">
        <div class="my-auto">
            <div class="border-l-4 accent-border pl-6 mb-8">
                <p class="font-serif text-lg italic text-gray-800 leading-relaxed">
                    "Every space tells a story. At DBD Studio, we believe retail and residential interiors should perform &mdash; not just impress."
                </p>
            </div>
            <p class="font-sans text-sm text-gray-600 font-light leading-relaxed mb-4">
                Founded and led by visionary designer Beulah Hephzibah, DBD Studio is a premier architectural and interior design firm specializing in creating high-performing retail and elegant residential environments.
            </p>
            <p class="font-sans text-sm text-gray-600 font-light leading-relaxed mb-6">
                We bridge the gap between building structure and interior soul, crafting spaces that influence consumer behavior, elevate brand prestige, and enhance daily living experiences.
            </p>
            
            <div class="grid grid-cols-2 gap-8 border-t border-gray-200 pt-6">
                <div>
                    <h3 class="font-sans text-xs tracking-wider text-gray-400 uppercase font-bold mb-2">Specialization</h3>
                    <p class="font-serif text-base text-gray-800 font-medium">Retail &amp; Residential Interiors</p>
                </div>
                <div>
                    <h3 class="font-sans text-xs tracking-wider text-gray-400 uppercase font-bold mb-2">Design Philosophy</h3>
                    <p class="font-serif text-base text-gray-800 font-medium">Aesthetic Elegance + Strategy</p>
                </div>
            </div>
        </div>
        {get_footer_element("02")}
    </div>
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "2.html"), "w") as f:
        f.write(slide2)

    # ------------------ SLIDE 3: VISION & MISSION ------------------
    slide3 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Our Vision & Mission", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">02 / Purpose</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Vision &amp; Mission</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="flex flex-row items-stretch gap-12">
            <!-- Vision Column -->
            <div class="w-1/2 bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between relative">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <div class="text-3xl accent-color mb-4"><i class="fas fa-eye"></i></div>
                    <h3 class="font-serif text-2xl font-bold text-gray-900 mb-4">Our Vision</h3>
                    <p class="font-sans text-gray-600 leading-relaxed font-light text-base">
                        To be a trailblazer in retail and residential interior design, shaping the future of branded environments that inspire, engage, and convert.
                    </p>
                </div>
                <div class="text-gray-100 text-6xl text-right font-serif font-bold">01</div>
            </div>
            
            <!-- Mission Column -->
            <div class="w-1/2 bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between relative">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <div class="text-3xl accent-color mb-4"><i class="fas fa-rocket"></i></div>
                    <h3 class="font-serif text-2xl font-bold text-gray-900 mb-4">Our Mission</h3>
                    <p class="font-sans text-gray-600 leading-relaxed font-light text-base">
                        To deliver transformative retail &amp; residential spaces that blend creativity, strategy, and sustainability, helping brands connect meaningfully with their customers.
                    </p>
                </div>
                <div class="text-gray-100 text-6xl text-right font-serif font-bold">02</div>
            </div>
        </div>
    </div>
    {get_footer_element("03")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "3.html"), "w") as f:
        f.write(slide3)

    # ------------------ SLIDE 4: DESIGN PHILOSOPHY ------------------
    slide4 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Design Philosophy", is_dark=False)}
<body>
<div class="slide-container flex flex-row">
    <!-- Left column: Philosophy Content -->
    <div class="w-50 h-full p-70 pb-40 flex flex-col justify-between relative">
        <div class="my-auto">
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-3">03 / Philosophy</span>
            <div class="accent-line"></div>
            <h1 class="font-serif text-4xl font-bold text-gray-900 mb-8 leading-tight">
                Strategic Design<br>That Performs
            </h1>
            
            <div class="space-y-6 text-gray-600 font-sans font-light leading-relaxed text-sm">
                <p>
                    A space is not just a container; it is a catalyst for performance, rest, and connection. Whether it's a high-stakes retail environment or a sanctuary for the home, every line drawn is an invitation to experience life more deeply.
                </p>
                <p class="border-l-2 accent-border pl-4 italic accent-color font-normal">
                    We focus on customer flow, sensory retail dynamics, and residential lifestyle optimization to ensure our designs perform.
                </p>
            </div>
        </div>
        {get_footer_element("04")}
    </div>
    
    <!-- Right column: Image -->
    <div class="w-50 h-full relative">
        <div class="absolute left-0 top-0 bottom-0 w-1.5 accent-bg z-20"></div>
        <div class="w-full h-full bg-cover bg-center" 
             style="background-image: url('../photo-video/new/the_trost_inside.jpeg');">
        </div>
        <div class="absolute inset-0 bg-gray-900 bg-opacity-20"></div>
    </div>
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "4.html"), "w") as f:
        f.write(slide4)

    # ------------------ SLIDE 5: PORTFOLIO OVERVIEW ------------------
    slide5 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Our Service Portfolio", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">04 / Services</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Our Portfolio</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="grid grid-cols-4 gap-6">
            <!-- Watches/Jewelry -->
            <div class="bg-white border border-gray-200 rounded-lg p-6 flex flex-col justify-between shadow-sm relative hover:shadow-md transition-all">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <span class="font-serif text-4xl font-bold text-gray-200 block mb-3">01</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Jewelry &amp; Luxury</h3>
                    <ul class="font-sans text-xs text-gray-500 space-y-2 leading-relaxed">
                        <li>&bull; Custom display cases</li>
                        <li>&bull; Precision lighting systems</li>
                        <li>&bull; Luxurious velvet finishes</li>
                        <li>&bull; Intimate client zones</li>
                    </ul>
                </div>
                <div class="text-right text-gray-300 text-lg mt-4"><i class="fas fa-gem"></i></div>
            </div>

            <!-- Apparel -->
            <div class="bg-white border border-gray-200 rounded-lg p-6 flex flex-col justify-between shadow-sm relative hover:shadow-md transition-all">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <span class="font-serif text-4xl font-bold text-gray-200 block mb-3">02</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Apparel &amp; Fashion</h3>
                    <ul class="font-sans text-xs text-gray-500 space-y-2 leading-relaxed">
                        <li>&bull; Identity integration</li>
                        <li>&bull; Flexible fixture systems</li>
                        <li>&bull; Custom fitting rooms</li>
                        <li>&bull; Dynamic storefronts</li>
                    </ul>
                </div>
                <div class="text-right text-gray-300 text-lg mt-4"><i class="fas fa-tshirt"></i></div>
            </div>

            <!-- Cafes -->
            <div class="bg-white border border-gray-200 rounded-lg p-6 flex flex-col justify-between shadow-sm relative hover:shadow-md transition-all">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <span class="font-serif text-4xl font-bold text-gray-200 block mb-3">03</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Cafes &amp; Dining</h3>
                    <ul class="font-sans text-xs text-gray-500 space-y-2 leading-relaxed">
                        <li>&bull; Cozy interior styling</li>
                        <li>&bull; Facade &amp; storefronts</li>
                        <li>&bull; Space-efficient layouts</li>
                        <li>&bull; Ambient &amp; task lighting</li>
                    </ul>
                </div>
                <div class="text-right text-gray-300 text-lg mt-4"><i class="fas fa-coffee"></i></div>
            </div>

            <!-- Residential -->
            <div class="bg-white border border-gray-200 rounded-lg p-6 flex flex-col justify-between shadow-sm relative hover:shadow-md transition-all">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <span class="font-serif text-4xl font-bold text-gray-200 block mb-3">04</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Premium Living</h3>
                    <ul class="font-sans text-xs text-gray-500 space-y-2 leading-relaxed">
                        <li>&bull; Bespoke living concepts</li>
                        <li>&bull; State-of-the-art kitchens</li>
                        <li>&bull; Customized master beds</li>
                        <li>&bull; Functional utility spaces</li>
                    </ul>
                </div>
                <div class="text-right text-gray-300 text-lg mt-4"><i class="fas fa-home"></i></div>
            </div>
        </div>
    </div>
    {get_footer_element("05")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "5.html"), "w") as f:
        f.write(slide5)

    # ------------------ SLIDE 6: TURNKEY SOLUTIONS ------------------
    slide6 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Turnkey Solutions", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">05 / Capabilities</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Single-Point Turnkey Delivery</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <!-- Horizontal steps -->
        <div class="relative flex flex-row justify-between items-start">
            <!-- Connector Line -->
            <div class="absolute bg-gray-200" style="top: 28px; left: 40px; right: 40px; height: 2px; z-index: 0;"></div>
            
            <!-- Step 1 -->
            <div class="z-10 flex flex-col items-center text-center" style="width: 22%;">
                <div class="rounded-full bg-white border-2 accent-border flex items-center justify-center text-gray-900 font-serif font-bold text-lg shadow-sm" style="width: 56px; height: 56px;">
                    01
                </div>
                <h3 class="font-serif text-base font-bold text-gray-900 mt-4 mb-2">Concept &amp; Design</h3>
                <p class="font-sans text-xs text-gray-500 leading-relaxed px-2">
                    Spatial blueprints, conceptual mood boards, and detailed 3D renderings matching brand rules.
                </p>
            </div>

            <!-- Step 2 -->
            <div class="z-10 flex flex-col items-center text-center" style="width: 22%;">
                <div class="rounded-full bg-white border-2 accent-border flex items-center justify-center text-gray-900 font-serif font-bold text-lg shadow-sm" style="width: 56px; height: 56px;">
                    02
                </div>
                <h3 class="font-serif text-base font-bold text-gray-900 mt-4 mb-2">Civil &amp; MEP Works</h3>
                <p class="font-sans text-xs text-gray-500 leading-relaxed px-2">
                    In-house electrical, mechanical, plumbing, and structural shell updates for precision safety.
                </p>
            </div>

            <!-- Step 3 -->
            <div class="z-10 flex flex-col items-center text-center" style="width: 22%;">
                <div class="rounded-full bg-white border-2 accent-border flex items-center justify-center text-gray-900 font-serif font-bold text-lg shadow-sm" style="width: 56px; height: 56px;">
                    03
                </div>
                <h3 class="font-serif text-base font-bold text-gray-900 mt-4 mb-2">Millwork &amp; Fixtures</h3>
                <p class="font-sans text-xs text-gray-500 leading-relaxed px-2">
                    Custom modular furniture, bespoke luxury displays, and custom glass fabrication.
                </p>
            </div>

            <!-- Step 4 -->
            <div class="z-10 flex flex-col items-center text-center" style="width: 22%;">
                <div class="rounded-full accent-bg flex items-center justify-center text-white font-serif font-bold text-lg shadow-sm" style="width: 56px; height: 56px;">
                    04
                </div>
                <h3 class="font-serif text-base font-bold text-gray-900 mt-4 mb-2">Handover</h3>
                <p class="font-sans text-xs text-gray-500 leading-relaxed px-2">
                    Quality inspection, final decorative styling, and ready-to-use retail or residential execution.
                </p>
            </div>
        </div>
    </div>
    {get_footer_element("06")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "6.html"), "w") as f:
        f.write(slide6)

    # ------------------ SLIDE 7: PROCESS ------------------
    slide7 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Our Collaborative Process", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">06 / Execution</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Our Collaborative Process</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="flex flex-row items-stretch gap-8">
            <!-- Step 1 -->
            <div class="w-1/3 bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between">
                <div>
                    <span class="font-serif text-4xl font-bold text-gray-200 block mb-4">01</span>
                    <h3 class="font-serif text-lg font-bold text-gray-900 mb-3">Client-First Collaboration</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed font-light">
                        We listen, interpret, and co-create. Your business metrics and personal preferences form the core foundation of our design strategy.
                    </p>
                </div>
                <div class="text-right text-gray-300 text-lg mt-4"><i class="fas fa-users"></i></div>
            </div>
            
            <!-- Step 2 -->
            <div class="w-1/3 bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between">
                <div>
                    <span class="font-serif text-4xl font-bold text-gray-200 block mb-4">02</span>
                    <h3 class="font-serif text-lg font-bold text-gray-900 mb-3">Innovation-Driven Design</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed font-light">
                        We integrate modern materials, smart spatial layouts, and premium lighting solutions to create unique, highly performing designs.
                    </p>
                </div>
                <div class="text-right text-gray-300 text-lg mt-4"><i class="fas fa-lightbulb"></i></div>
            </div>
            
            <!-- Step 3 -->
            <div class="w-1/3 bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between">
                <div>
                    <span class="font-serif text-4xl font-bold text-gray-200 block mb-4">03</span>
                    <h3 class="font-serif text-lg font-bold text-gray-900 mb-3">Detail-Oriented Execution</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed font-light">
                        Our engineering precision ensures that projects are delivered with superior craftsmanship, on schedule, and within budget parameters.
                    </p>
                </div>
                <div class="text-right text-gray-300 text-lg mt-4"><i class="fas fa-check-double"></i></div>
            </div>
        </div>
    </div>
    {get_footer_element("07")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "7.html"), "w") as f:
        f.write(slide7)

    # ------------------ SLIDE 8: ADVANTAGES ------------------
    slide8 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Competitive Advantages", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">07 / Advantages</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Why Partner with DBD Studio?</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="grid grid-cols-2 gap-6">
            <!-- Advantage 1 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-row items-start gap-4">
                <div class="text-2xl accent-color mt-1"><i class="fas fa-drafting-compass"></i></div>
                <div>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Architectural Foundation</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed">
                        Beulah Hephzibah's architectural and civil background ensures that designs are structurally sound, compliant, and highly functional.
                    </p>
                </div>
            </div>

            <!-- Advantage 2 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-row items-start gap-4">
                <div class="text-2xl accent-color mt-1"><i class="fas fa-hammer"></i></div>
                <div>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-2">In-House Execution Teams</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed">
                        By employing our own carpenters, painters, and MEP technicians, we bypass subcontractor delays and enforce absolute quality control.
                    </p>
                </div>
            </div>

            <!-- Advantage 3 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-row items-start gap-4">
                <div class="text-2xl accent-color mt-1"><i class="fas fa-truck-loading"></i></div>
                <div>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Direct Material Sourcing</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed">
                        Our direct wholesale partnerships with glass, metal, and wood distributors allow us to provide premium finishes at optimized budgets.
                    </p>
                </div>
            </div>

            <!-- Advantage 4 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-row items-start gap-4">
                <div class="text-2xl accent-color mt-1"><i class="fas fa-leaf"></i></div>
                <div>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Sustainable Practices</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed">
                        We source responsibly, incorporate energy-efficient lighting solutions, and choose low-VOC materials for eco-friendly compliance.
                    </p>
                </div>
            </div>
        </div>
    </div>
    {get_footer_element("08")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "8.html"), "w") as f:
        f.write(slide8)

    # ------------------ SLIDE 9: CASE STUDY: JEWELRY & BOUTIQUE ------------------
    slide9 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Jewelry & Boutique Excellence", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">08 / Case Studies</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Jewelry &amp; Boutique Excellence</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="flex flex-row gap-8">
            <!-- Case Study 1 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 bg-cover bg-center" style="background-image: url('../photo-video/WhatsApp Image 2025-08-11 at 10.51.32 (2).jpeg');"></div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">S.L. Shet Diamond House</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            A premium jewelry showroom in Mangalore. Designed with secure luxury showcases, sophisticated custom glass fabrication, and specialized spotlighting layout designed to highlight precious stones.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Luxury Retail</span>
                    </div>
                </div>
            </div>

            <!-- Case Study 2 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 bg-cover bg-center" style="background-image: url('../photo-video/FRANGIPANI.jpeg');"></div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Frangipani</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            An intimate boutique shopping environment. The design prioritizes warm luxury, custom metal fixture systems, and customer flow optimization that increases browsing time and brand engagement.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Boutique Concept</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {get_footer_element("09")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "9.html"), "w") as f:
        f.write(slide9)

    # ------------------ SLIDE 10: CASE STUDY: APPAREL & LIFESTYLE ------------------
    slide10 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Apparel & Lifestyle Design", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">09 / Case Studies</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Apparel &amp; Lifestyle Design</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="flex flex-row gap-8">
            <!-- Case Study 1 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 bg-cover bg-center" style="background-image: url('../photo-video/CHUMBAK.jpeg');"></div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Chumbak</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            Vibrant and colorful conceptual retail space design. Emphasizes flexible product shelving systems, highly creative visual merchandising areas, and bold color blocking to showcase the brand's unique lifestyle products.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Fashion &amp; Lifestyle</span>
                    </div>
                </div>
            </div>

            <!-- Case Study 2 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 bg-cover bg-center" style="background-image: url('../photo-video/SIGNATURE FELICITY.jpeg');"></div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Signature Felicity</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            A modern retail storefront and display system. Highlights clean lines, premium wooden textures, and an open layout that draws foot traffic and facilitates product visibility from all key angles.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Premium Retail</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {get_footer_element("10")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "10.html"), "w") as f:
        f.write(slide10)

    # ------------------ SLIDE 11: CASE STUDY: F&B CAFE PART 1 ------------------
    slide11 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("F&B & Cafe Design - Part 1", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">10 / Case Studies</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Hospitality &amp; Dining Spaces &mdash; Part I</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="flex flex-row gap-8">
            <!-- Case Study 1 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 flex flex-row">
                    <div class="w-1/2 h-full bg-cover bg-center" style="background-image: url('../photo-video/new/brown_boy_cafe.jpeg');"></div>
                    <div class="w-1/2 h-full bg-cover bg-center" style="background-image: url('../photo-video/new/brown_boy_cafe_interior.jpeg');"></div>
                </div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Brown Boy Cafe</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            An industrial cozy coffee shop featuring a striking modern dark steel facade outside, paired with warm lighting, wood and brick textures inside to create an inviting neighborhood hang-out.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Cozy Cafe &amp; Facade</span>
                    </div>
                </div>
            </div>

            <!-- Case Study 2 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 flex flex-row">
                    <div class="w-1/2 h-full bg-cover bg-center" style="background-image: url('../photo-video/new/the_trost_outside.jpeg');"></div>
                    <div class="w-1/2 h-full bg-cover bg-center" style="background-image: url('../photo-video/new/the_trost_inside.jpeg');"></div>
                </div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">The Trost</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            A contemporary dining setup. The exterior facade uses sleek black grids and large glass panels, opening into an elegant, high-end seating arrangement that provides a premium dining feel.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Fine Dining Restaurant</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {get_footer_element("11")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "11.html"), "w") as f:
        f.write(slide11)

    # ------------------ SLIDE 12: CASE STUDY: F&B CAFE PART 2 ------------------
    slide12 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("F&B & Cafe Design - Part 2", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">11 / Case Studies</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Hospitality &amp; Dining Spaces &mdash; Part II</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="flex flex-row gap-8">
            <!-- Case Study 1 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 flex flex-row">
                    <div class="w-1/2 h-full bg-cover bg-center" style="background-image: url('../photo-video/new/sandowitch_outsideview.jpeg');"></div>
                    <div class="w-1/2 h-full bg-cover bg-center" style="background-image: url('../photo-video/new/sandowitch_inside_view.jpeg');"></div>
                </div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Sandowitch</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            An eye-catching, high-contrast storefront layout. Focuses on space optimization for fast-casual ordering, modern counter styling, and clean sanitary-themed white and orange aesthetics.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Fast Casual Cafe</span>
                    </div>
                </div>
            </div>

            <!-- Case Study 2 -->
            <div class="w-1/2 bg-white border border-gray-200 rounded-lg overflow-hidden shadow-sm flex flex-col justify-between h-340">
                <div class="h-170 bg-cover bg-center" style="background-image: url('../photo-video/WhatsApp Image 2025-08-11 at 10.51.35 (1).jpeg');"></div>
                <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                        <h3 class="font-serif text-base font-bold text-gray-900 mb-2">Cafe Murmura</h3>
                        <p class="font-sans text-gray-500 leading-relaxed text-11">
                            A cozy and artistic cafe layout. Reconciles raw wood elements, customized metal stools, and a warm, low-contrast color palette to cultivate a relaxed, boutique dining feel.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex justify-between items-center text-10">
                        <span class="font-sans uppercase tracking-wider text-gray-400 font-bold">Category</span>
                        <span class="font-sans font-bold accent-color uppercase">Boutique Cafe</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {get_footer_element("12")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "12.html"), "w") as f:
        f.write(slide12)

    # ------------------ SLIDE 13: DHOBILITE ------------------
    slide13 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Commercial Turnkey - Dhobilite", is_dark=False)}
<body>
<div class="slide-container flex flex-row">
    <!-- Left column: Image -->
    <div class="w-50 h-full relative">
        <div class="w-full h-full bg-cover bg-center" 
             style="background-image: url('../photo-video/DHOBILITE.jpeg');">
        </div>
        <div class="absolute inset-0 bg-gray-900 bg-opacity-10"></div>
    </div>

    <!-- Right column: Content -->
    <div class="w-50 h-full p-70 pb-40 flex flex-col justify-between relative">
        <div class="absolute top-0 left-0 w-1 accent-bg h-1/5"></div>
        <div class="my-auto">
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-3">12 / Commercial Roll-outs</span>
            <div class="accent-line"></div>
            <h1 class="font-serif text-4xl font-bold text-gray-900 mb-6 leading-tight">
                Turnkey Roll-outs:<br>Dhobilite
            </h1>
            
            <p class="font-sans text-sm text-gray-600 font-light leading-relaxed mb-4">
                Dhobilite is a leading laundry and dry-cleaning franchise. DBD Studio has served as their trusted design partner, delivering scalable, turnkey spatial fit-outs across multiple locations.
            </p>
            <p class="font-sans text-xs text-gray-500 font-light leading-relaxed mb-6">
                Our standardized layout templates optimize operations, ensure brand identity consistency across regions, and support rapid, cost-effective franchise launch roll-outs.
            </p>
            
            <div class="grid grid-cols-2 gap-6 border-t border-gray-200 pt-6">
                <div>
                    <h3 class="font-sans text-xs tracking-wider text-gray-400 uppercase font-bold mb-1">Focus</h3>
                    <p class="font-serif text-base text-gray-800 font-medium">Scalable Brand Templates</p>
                </div>
                <div>
                    <h3 class="font-sans text-xs tracking-wider text-gray-400 uppercase font-bold mb-1">Service Type</h3>
                    <p class="font-serif text-base text-gray-800 font-medium">Turnkey Roll-out Execution</p>
                </div>
            </div>
        </div>
        {get_footer_element("13")}
    </div>
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "13.html"), "w") as f:
        f.write(slide13)

    # ------------------ SLIDE 14: STRATEGIC RETAIL POSITIONING ------------------
    slide14 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Strategic Retail Positioning", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">13 / Retail Formats</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Strategic Retail Positioning</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="grid grid-cols-4 gap-6">
            <!-- format 1 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-col justify-between h-280">
                <div>
                    <span class="font-sans font-bold text-gray-400 block mb-2 text-10">01 / BRAND DESTINATION</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Luxury Flagships</h3>
                    <p class="font-sans text-gray-500 leading-relaxed text-11">
                        Premium custom finishes, highly specialized conceptual design, and immersive spatial layout designed for high brand impact.
                    </p>
                </div>
            </div>

            <!-- format 2 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-col justify-between h-280">
                <div>
                    <span class="font-sans font-bold text-gray-400 block mb-2 text-10">02 / IMMERSIVE BOUTIQUE</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Concept Boutiques</h3>
                    <p class="font-sans text-gray-500 leading-relaxed text-11">
                        Bespoke spatial details, customized metal &amp; wood fixtures, and intimate layouts designed for optimal customer flow.
                    </p>
                </div>
            </div>

            <!-- format 3 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-col justify-between h-280">
                <div>
                    <span class="font-sans font-bold text-gray-400 block mb-2 text-10">03 / RAPID LAUNCH</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Roll-out Storefronts</h3>
                    <p class="font-sans text-gray-500 leading-relaxed text-11">
                        Modular, cost-effective templates designed for rapid assembly, ensuring brand consistency across franchise locations.
                    </p>
                </div>
            </div>

            <!-- format 4 -->
            <div class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm flex flex-col justify-between h-280">
                <div>
                    <span class="font-sans font-bold text-gray-400 block mb-2 text-10">04 / COMPACT IMPRESSION</span>
                    <h3 class="font-serif text-base font-bold text-gray-900 mb-3">Shop-in-Shops</h3>
                    <p class="font-sans text-gray-500 leading-relaxed text-11">
                        Highly optimized layouts designed to maximize compact department store spaces with high brand visibility and fixture density.
                    </p>
                </div>
            </div>
        </div>
    </div>
    {get_footer_element("14")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "14.html"), "w") as f:
        f.write(slide14)

    # ------------------ SLIDE 15: METRICS ------------------
    slide15 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Design Excellence Metrics", is_dark=False)}
<body>
<div class="slide-container slide-container-padded">
    <div class="slide-header">
        <div>
            <span class="font-sans text-xs tracking-widest text-gray-500 uppercase block mb-2">14 / Track Record</span>
            <h2 class="font-serif text-3xl font-bold text-gray-900">Design Excellence Metrics</h2>
        </div>
        <div class="accent-line"></div>
    </div>
    
    <div class="slide-body">
        <div class="grid grid-cols-3 gap-8">
            <!-- Metric 1 -->
            <div class="bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between relative">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <span class="font-sans text-6xl font-bold accent-color block mb-3">100+</span>
                    <h3 class="font-serif text-lg font-bold text-gray-900 mb-2">Projects Completed</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed">
                        From boutique retail stores to luxury residential curations, delivered with precision across South India.
                    </p>
                </div>
            </div>

            <!-- Metric 2 -->
            <div class="bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between relative">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <span class="font-sans text-6xl font-bold accent-color block mb-3">15+</span>
                    <h3 class="font-serif text-lg font-bold text-gray-900 mb-2">Brand Partners</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed">
                        Collaborative partnerships with retail, food &amp; beverage, and commercial franchise companies.
                    </p>
                </div>
            </div>

            <!-- Metric 3 -->
            <div class="bg-white border border-gray-200 p-8 rounded-lg shadow-sm flex flex-col justify-between relative">
                <div class="absolute top-0 left-0 w-full h-1 accent-bg rounded-t-lg"></div>
                <div>
                    <span class="font-sans text-6xl font-bold accent-color block mb-3">5</span>
                    <h3 class="font-serif text-lg font-bold text-gray-900 mb-2">Core Categories</h3>
                    <p class="font-sans text-xs text-gray-500 leading-relaxed">
                        Specialized capabilities in Jewelry, Apparel, Cafes &amp; Restaurants, Commercial Turnkey, and Premium Residential.
                    </p>
                </div>
            </div>
        </div>
    </div>
    {get_footer_element("15")}
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "15.html"), "w") as f:
        f.write(slide15)

    # ------------------ SLIDE 16: CONTACT ------------------
    slide16 = f"""<!DOCTYPE html>
<html lang="en">
{get_header("Contact Us - DBD Studio", is_dark=True)}
<body>
<div class="slide-container flex flex-row">
    <!-- Left panel (Text) -->
    <div class="w-55 h-full p-80 pb-40 flex flex-col justify-between relative z-10">
        <div>
            <div class="accent-line"></div>
            <span class="font-sans text-xs tracking-widest text-gray-400 uppercase block mb-3">15 / Get In Touch</span>
            <h1 class="font-serif text-5xl font-bold text-white mb-8 leading-tight">
                Let's Create<br>Something<br>
                <span class="accent-color italic">Remarkable</span>
            </h1>
            <p class="font-sans text-sm text-gray-400 leading-relaxed max-w-90 border-l-2 accent-border pl-6">
                Ready to transform your retail presence or residential space? Reach out to our design and engineering team to schedule a detailed session.
            </p>
        </div>
        <div class="font-sans text-xs tracking-wider text-gray-500 uppercase flex justify-between items-end border-t border-gray-800 pt-6">
            <p>&copy; 2026 Dream Build Design Studio &bull; Company Profile</p>
            <p class="page-num font-bold">16</p>
        </div>
    </div>
    
    <!-- Right panel (Contact details) -->
    <div class="w-45 h-full bg-gray-900 bg-opacity-80 p-70 flex flex-col justify-center relative">
        <div class="absolute left-0 top-0 bottom-0 w-1 accent-bg"></div>
        <div class="space-y-6">
            <!-- Address -->
            <div class="flex items-start">
                <div class="rounded-lg bg-gray-800 border border-gray-700 text-sm accent-color flex items-center justify-center mr-4 flex-shrink-0" style="width: 40px; height: 40px;">
                    <i class="fas fa-map-marker-alt"></i>
                </div>
                <div>
                    <h4 class="font-sans tracking-widest text-gray-400 uppercase font-bold mb-1 text-10">Visit Us</h4>
                    <p class="font-serif text-sm text-white">No. 15/1, GK Layout, 4th Cross</p>
                    <p class="font-sans text-gray-400 mt-0.5 text-10">Electronic City, Bangalore - 560100</p>
                </div>
            </div>

            <!-- Phone -->
            <div class="flex items-start">
                <div class="rounded-lg bg-gray-800 border border-gray-700 text-sm accent-color flex items-center justify-center mr-4 flex-shrink-0" style="width: 40px; height: 40px;">
                    <i class="fas fa-phone-alt"></i>
                </div>
                <div>
                    <h4 class="font-sans tracking-widest text-gray-400 uppercase font-bold mb-1 text-10">Call Us</h4>
                    <p class="font-serif text-sm text-white">+91 63617 36075</p>
                </div>
            </div>

            <!-- Email -->
            <div class="flex items-start">
                <div class="rounded-lg bg-gray-800 border border-gray-700 text-sm accent-color flex items-center justify-center mr-4 flex-shrink-0" style="width: 40px; height: 40px;">
                    <i class="fas fa-envelope"></i>
                </div>
                <div>
                    <h4 class="font-sans tracking-widest text-gray-400 uppercase font-bold mb-1 text-10">Email Us</h4>
                    <p class="font-serif text-sm text-white">dreambuilddesign@outlook.com</p>
                </div>
            </div>
            
            <!-- Working Hours -->
            <div class="flex items-start">
                <div class="rounded-lg bg-gray-800 border border-gray-700 text-sm accent-color flex items-center justify-center mr-4 flex-shrink-0" style="width: 40px; height: 40px;">
                    <i class="fas fa-clock"></i>
                </div>
                <div>
                    <h4 class="font-sans tracking-widest text-gray-400 uppercase font-bold mb-1 text-10">Hours</h4>
                    <p class="font-sans text-gray-300 text-11">Mon &ndash; Fri: 9:00 AM &ndash; 6:00 PM</p>
                    <p class="font-sans text-gray-300 mt-0.5 text-11">Sat: 10:00 AM &ndash; 4:00 PM</p>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""
    with open(os.path.join(output_dir, "16.html"), "w") as f:
        f.write(slide16)

    print("Successfully generated all 16 slides.")

if __name__ == "__main__":
    main()
