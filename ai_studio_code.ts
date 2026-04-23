export interface Lecture {
  id: number;
  title: string;
  doctor: string;
  links: {
    report?: string | string[];
    recording?: string | string[];
    material?: string | string[];
    transcription?: string | string[];
  };
}

export const lectures: Lecture[] = [
  {
    id: 1,
    title: "Anatomy & physiology of ear",
    doctor: "د.فؤاد شمسان",
    links: {
      report: "https://t.me/september216thbatchENT/58",
      recording: "https://t.me/september216thbatchENT/56",
      material: "https://t.me/september216thbatchENT/55"
    }
  },
  // ... سيتم تضمين جميع المحاضرات الـ 16 هنا
  {
    id: 16,
    title: "Neck Mass & ENT Tumors",
    doctor: "د.خالد الطهيف",
    links: {
      material: "https://t.me/september216thbatchENT/137",
      report: "https://t.me/september216thbatchENT/137",
      recording: "https://t.me/september216thbatchENT/137"
    }
  }
];