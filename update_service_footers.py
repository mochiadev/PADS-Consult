import os
import re

# The new footer content adapted with relative paths
new_footer = """<footer class="bg-brand-secondary text-white pt-12 pb-6">
            <div class="container mx-auto px-6">
                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-8">
                    <!-- Company Info -->
                    <div>
                        <img
                            src="../assets/images/footerlogo.png"
                            alt="PAD Consult"
                            class="h-16 md:h-20 lg:h-24 w-auto mb-4"
                        />
                        <p class="text-gray-400 leading-relaxed text-sm mb-4">
                            Delivering high-quality audit, tax, and advisory
                            services with a focus on building long-term
                            relationships.
                        </p>
                        <div class="flex gap-3">
                            <a
                                href="#"
                                class="w-9 h-9 bg-white/10 rounded-full flex items-center justify-center hover:bg-brand-lightBlue transition-colors"
                            >
                                <i class="ph ph-facebook-logo"></i>
                            </a>
                            <a
                                href="#"
                                class="w-9 h-9 bg-white/10 rounded-full flex items-center justify-center hover:bg-brand-lightBlue transition-colors"
                            >
                                <i class="ph ph-linkedin-logo"></i>
                            </a>
                            <a
                                href="#"
                                class="w-9 h-9 bg-white/10 rounded-full flex items-center justify-center hover:bg-brand-lightBlue transition-colors"
                            >
                                <i class="ph ph-twitter-logo"></i>
                            </a>
                        </div>
                    </div>

                    <!-- Services -->
                    <div>
                        <h4 class="text-lg font-bold mb-4 text-brand-gold">
                            Our Services
                        </h4>
                        <ul class="space-y-2 text-gray-400 text-sm">
                            <li>
                                <a
                                    href="audit-accounting.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Audit & Accounting</a
                                >
                            </li>
                            <li>
                                <a
                                    href="tax-advisory.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Tax Advisory & Outsourcing</a
                                >
                            </li>
                            <li>
                                <a
                                    href="company-secretarial.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Company Secretarial Services</a
                                >
                            </li>
                            <li>
                                <a
                                    href="financial-management.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Financial Management & Consulting</a
                                >
                            </li>
                            <li>
                                <a
                                    href="business-planning.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Business Planning</a
                                >
                            </li>
                            <li>
                                <a
                                    href="capacity-building.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Organizational Capacity Building</a
                                >
                            </li>
                        </ul>
                    </div>

                    <!-- Quick Links -->
                    <div>
                        <h4 class="text-lg font-bold mb-4 text-brand-gold">
                            Quick Links
                        </h4>
                        <ul class="space-y-2 text-gray-400 text-sm">
                            <li>
                                <a
                                    href="../index.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Home</a
                                >
                            </li>
                            <li>
                                <a
                                    href="../about.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >About Us</a
                                >
                            </li>
                            <li>
                                <a
                                    href="../services.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Services</a
                                >
                            </li>
                            <li>
                                <a
                                    href="../enterprise.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Software Training</a
                                >
                            </li>

                            <li>
                                <a
                                    href="../contact.html"
                                    class="hover:text-brand-lightBlue transition-colors flex items-center gap-2"
                                    ><i class="ph ph-caret-right text-xs"></i
                                    >Contact</a
                                >
                            </li>
                        </ul>
                    </div>

                    <!-- Contact -->
                    <div>
                        <h4 class="text-lg font-bold mb-4 text-brand-gold">
                            Contact Us
                        </h4>
                        <ul class="space-y-3 text-gray-400 text-sm">
                            <li class="flex items-start gap-3">
                                <i
                                    class="ph ph-map-pin text-brand-lightBlue text-lg mt-0.5"
                                ></i>
                                <span
                                    >MRQH+JGP, Ritz Junction,<br />Madina Adenta
                                    High Way, Accra</span
                                >
                            </li>
                            <li
                                class="flex flex-col gap-1"
                                x-data="{ expanded: false }"
                            >
                                <div class="flex items-center gap-3">
                                    <i
                                        class="ph ph-phone text-brand-lightBlue text-lg"
                                    ></i>
                                    <span>024 591 2363 / 055 274 4179</span>
                                    <button
                                        @click="expanded = !expanded"
                                        class="hover:text-brand-lightBlue transition-colors focus:outline-none"
                                        aria-label="Toggle more phone numbers"
                                    >
                                        <i
                                            class="ph"
                                            :class="expanded ? 'ph-caret-up' : 'ph-caret-down'"
                                        ></i>
                                    </button>
                                </div>
                                <div
                                    x-show="expanded"
                                    x-collapse
                                    class="pl-8 text-gray-400 text-sm"
                                >
                                    <span>024 166 2867 / 054 236 5050</span>
                                </div>
                            </li>
                            <li class="flex items-center gap-3">
                                <i
                                    class="ph ph-envelope text-brand-lightBlue text-lg"
                                ></i>
                                <a
                                    href="mailto:padconsults@gmail.com"
                                    class="hover:text-brand-lightBlue transition-colors"
                                    >padconsults@gmail.com</a
                                >
                            </li>
                        </ul>
                    </div>
                </div>

                <div
                    class="border-t border-gray-800 pt-6 text-center text-gray-500 text-sm"
                >
                    <p>
                        &copy; <span id="currentYear"></span> PAD Consult
                        Services. All rights reserved.
                    </p>
                </div>
            </div>
        </footer>"""

services_dir = r"d:\WorkSpace\PAD Consult\services"
files = [
    "audit-accounting.html",
    "tax-advisory.html",
    "company-secretarial.html",
    "financial-management.html",
    "business-planning.html",
    "capacity-building.html"
]

for filename in files:
    file_path = os.path.join(services_dir, filename)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find footer tag and its content
        # Using DOTALL so . matches newlines
        pattern = re.compile(r'<footer.*?</footer>', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(new_footer, content)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated footer in {filename}")
        else:
            print(f"No footer found in {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")
