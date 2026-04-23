from flask import Flask, render_template_string

app = Flask(__name__)

# بيانات المحاضرات
LECTURES = [
    {"id": 1, "title": "Anatomy & physiology of ear", "doctor": "د.فؤاد شمسان", "links": {"report": "https://t.me/september216thbatchENT/58", "recording": "https://t.me/september216thbatchENT/56", "material": "https://t.me/september216thbatchENT/55"}},
    {"id": 2, "title": "Symptomatology & examination & Assessment of Ear", "doctor": "د.فؤاد شمسان", "links": {"report": "https://t.me/september216thbatchENT/59", "recording": "https://t.me/september216thbatchENT/57", "material": "https://t.me/september216thbatchENT/55"}},
    {"id": 3, "title": "Otosclerosis, Otitic Barotrauma and Facial nerve", "doctor": "د.حنان داؤود", "links": {"report": "https://t.me/september216thbatchENT/75", "recording": "https://t.me/september216thbatchENT/60", "material": "https://t.me/september216thbatchENT/73"}},
    {"id": 4, "title": "Diseases of Inner ear and Anatomy & Physiology of Nose & PNS", "doctor": "د.حنان داؤود", "links": {"report": "https://t.me/september216thbatchENT/74", "recording": "https://t.me/september216thbatchENT/62", "material": "https://t.me/september216thbatchENT/73"}},
    {"id": 5, "title": "Diseases of External Ear", "doctor": "د. ضياء السروري", "links": {"report": "https://t.me/september216thbatchENT/77", "recording": "https://t.me/september216thbatchENT/63", "material": "https://t.me/september216thbatchENT/78"}},
    {"id": 6, "title": "Acute Otitis media", "doctor": "د.زيد المراني", "links": {"report": "https://t.me/september216thbatchENT/110", "material": "https://t.me/september216thbatchENT/101"}},
    {"id": 7, "title": "Anatomy and physiology of the larynx", "doctor": "د.خالد عثرب", "links": {"report": "https://t.me/september216thbatchENT/87", "recording": "https://t.me/september216thbatchENT/79", "material": "https://t.me/september216thbatchENT/83"}},
    {"id": 8, "title": "Tracheostomy", "doctor": "د.خالد عثرب", "links": {"report": "https://t.me/september216thbatchENT/88", "recording": "https://t.me/september216thbatchENT/80", "material": "https://t.me/september216thbatchENT/84", "transcription": "https://t.me/september216thbatchENT/85"}},
    {"id": 9, "title": "Diseases of Larynx", "doctor": "د.سلوى الحمادي", "links": {"report": "https://t.me/september216thbatchENT/89", "recording": "https://t.me/september216thbatchENT/81", "material": "https://t.me/september216thbatchENT/86"}},
    {"id": 10, "title": "Rhinosinusitis", "doctor": "د.نجلاء المقالح", "links": {"report": "https://t.me/september216thbatchENT/91", "recording": "https://t.me/september216thbatchENT/90", "material": "https://t.me/september216thbatchENT/98"}},
    {"id": 11, "title": "Chronic Otitis media", "doctor": "د.زيد المراني", "links": {"report": "https://t.me/september216thbatchENT/159", "material": "https://t.me/september216thbatchENT/151"}},
    {"id": 12, "title": "Anatomy and physiology of oral cavity & pharynx", "doctor": "د.جديس الحكيمي", "links": {"report": "https://t.me/september216thbatchENT/122", "material": "https://t.me/september216thbatchENT/123"}},
    {"id": 13, "title": "Adenoidotonsillar disease", "doctor": "د.جديس الحكيمي", "links": {"recording": "https://t.me/september216thbatchENT/138", "material": "https://t.me/september216thbatchENT/140"}},
    {"id": 14, "title": "Trauma and FB", "doctor": "د.خلدون الجبيلي", "links": {"report": "https://t.me/september216thbatchENT/118", "recording": "https://t.me/september216thbatchENT/117", "material": "https://t.me/september216thbatchENT/119"}},
    {"id": 15, "title": "Deep neck spaces infections and Update in ENT", "doctor": "د.سلوى الحمادي", "links": {"report": "https://t.me/september216thbatchENT/126", "recording": "https://t.me/september216thbatchENT/124", "material": "https://t.me/september216thbatchENT/125"}},
    {"id": 16, "title": "DNS, Allergic & non-allergic Rhinits, Neck Mass & ENT Tumors", "doctor": "د.خالد الطهيف", "links": {"material": "https://t.me/september216thbatchENT/137"}}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>فهرس قسم الـ ENT</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Almarai:wght@300;400;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { font-family: 'Almarai', sans-serif; overflow-x: hidden; }
        .mobile-frame { max-width: 450px; margin: 0 auto; min-height: 100vh; background: #F8F9FB; position: relative; }
        .glass { background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); }
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-thumb { background: #E5E7EB; border-radius: 10px; }
    </style>
</head>
<body class="bg-gray-100">
    <div class="mobile-frame shadow-2xl overflow-hidden flex flex-col">
        
        <!-- Splash Screen Screen (Initially shown) -->
        <div id="splash" class="flex flex-col items-center justify-center p-8 text-center bg-[#FAF7F2] absolute inset-0 z-50 transition-all duration-500">
            <div class="relative w-40 h-40 mb-8 bg-white rounded-full shadow-xl flex items-center justify-center p-4">
                <img src="https://cdn-icons-png.flaticon.com/512/3063/3063061.png" class="w-full opacity-80" alt="logo">
            </div>
            <h1 class="text-3xl font-extrabold text-blue-600 mb-2">✨ فهرس قسم الـ ENT ✨</h1>
            <p class="text-blue-500 font-medium mb-8">مرحباً بكم في تطبيق الفهرس الشامل</p>
            <p class="text-gray-500 text-sm mb-12">يتضمن الفهرس التسجيلات الصوتية، الملازم، التقارير، والتفريغات الخاصة بالمادة</p>
            <p class="text-gray-400 text-xs mb-4">اللجنة العلمية للدفعة السادسة</p>
            <button onclick="startApp()" class="w-full bg-orange-500 text-white font-bold py-4 rounded-2xl shadow-lg active:scale-95 transition-transform">ابدأ التصفح</button>
        </div>

        <!-- Main Content -->
        <div id="main-content" class="hidden flex flex-col h-screen">
            <!-- Header -->
            <header class="px-6 pt-10 pb-4 bg-[#F8F9FB] sticky top-0 z-40">
                <h2 class="text-xl font-bold text-gray-800 text-center mb-6">فهرس المحاضرات</h2>
                <div class="relative">
                    <input id="search" type="text" placeholder="البحث عن محاضرة أو دكتور..." class="w-full bg-white border border-gray-100 shadow-sm rounded-2xl py-3 px-12 text-sm outline-none focus:ring-2 focus:ring-blue-500 transition-all">
                    <div class="absolute right-2 top-1/2 -translate-y-1/2 w-9 h-9 bg-orange-500 rounded-xl flex items-center justify-center text-white">
                        <i data-lucide="search" size="18"></i>
                    </div>
                </div>
            </header>

            <!-- List -->
            <div id="lecture-list" class="flex-1 overflow-y-auto px-6 pb-28 pt-2">
                <!-- Records will be injected here -->
            </div>

            <!-- Bottom Navigation -->
            <nav class="fixed bottom-0 left-0 right-0 max-w-[450px] mx-auto bg-white border-t border-gray-100 py-3 flex justify-around items-center rounded-t-[30px] shadow-lg z-50">
                <div class="flex flex-col items-center text-orange-500"><i data-lucide="layout-grid"></i><span class="text-[10px] font-bold">Index</span></div>
                <div class="flex flex-col items-center text-gray-300"><i data-lucide="search"></i><span class="text-[10px] font-bold">Search</span></div>
                <div class="flex flex-col items-center text-gray-300"><i data-lucide="user"></i><span class="text-[10px] font-bold">Profile</span></div>
            </nav>
        </div>
    </div>

    <script>
        const lectures = {{ lectures_json | safe }};
        
        function startApp() {
            document.getElementById('splash').classList.add('opacity-0', 'pointer-events-none');
            document.getElementById('main-content').classList.remove('hidden');
            setTimeout(() => document.getElementById('splash').remove(), 500);
            renderLectures(lectures);
        }

        function createCard(lec) {
            return `
                <div class="bg-white rounded-3xl p-5 shadow-sm border border-gray-50 mb-4 animate-in fade-in slide-in-from-bottom-4 duration-300">
                    <div class="flex justify-between items-start mb-4">
                        <div class="flex-1">
                            <div class="flex items-center gap-2 mb-1">
                                <span class="bg-blue-600 text-white w-7 h-7 rounded-lg flex items-center justify-center text-xs font-bold font-sans">${lec.id}</span>
                                <h3 class="text-sm font-bold text-gray-800">${lec.doctor}</h3>
                            </div>
                            <p class="text-xs text-gray-500 font-medium leading-relaxed">${lec.title}</p>
                        </div>
                        <i data-lucide="chevron-left" class="text-gray-300 w-5"></i>
                    </div>
                    <div class="flex justify-around items-center pt-2 border-t border-gray-50">
                        ${renderLink(lec.links.material, 'book', 'الملزمة', 'bg-blue-500')}
                        ${renderLink(lec.links.recording, 'mic', 'التسجيل', 'bg-orange-500')}
                        ${renderLink(lec.links.report, 'file-text', 'التقرير', 'bg-yellow-500')}
                        ${renderLink(lec.links.transcription, 'pen-tool', 'التفريغات', 'bg-emerald-500')}
                    </div>
                </div>
            `;
        }

        function renderLink(url, icon, label, color) {
            if (!url) return `<div class="flex flex-col items-center opacity-20 grayscale"><div class="w-10 h-10 rounded-xl flex items-center justify-center bg-gray-200 text-white"><i data-lucide="${icon}" size="18"></i></div><span class="text-[9px] mt-1 font-bold">${label}</span></div>`;
            const finalUrl = Array.isArray(url) ? url[0] : url;
            return `
                <a href="${finalUrl}" target="_blank" class="flex flex-col items-center group transition-transform active:scale-90">
                    <div class="w-11 h-11 rounded-xl flex items-center justify-center ${color} text-white shadow-md">
                        <i data-lucide="${icon}" size="18"></i>
                    </div>
                    <span class="text-[10px] mt-1 text-gray-600 font-bold">${label}</span>
                </a>
            `;
        }

        function renderLectures(data) {
            const container = document.getElementById('lecture-list');
            container.innerHTML = data.map(createCard).join('');
            lucide.createIcons();
        }

        document.getElementById('search').addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            const filtered = lectures.filter(l => 
                l.title.toLowerCase().includes(query) || 
                l.doctor.includes(query)
            );
            renderLectures(filtered);
        });

        lucide.createIcons();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    import json
    return render_template_string(HTML_TEMPLATE, lectures_json=json.dumps(LECTURES))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)