from fpdf import FPDF

# Create the PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Next.js Dynamic Route Data Fetching Guide", ln=True, align="C")
pdf.ln(10)

# Body content
content = """
Example: Fetching a Cabin by ID

lib/api.ts
-----------------------------------
export async function getCabin(id: string) {
  const res = await fetch(`https://example.com/api/cabins/${id}`);
  if (!res.ok) throw new Error('Failed to fetch cabin data');
  return res.json();
}

-----------------------------------
app/cabins/[id]/page.tsx
-----------------------------------
import { getCabin } from '@/lib/api';

interface CabinDetailPageProps {
  params: Promise<{ id: string }>;
}

export default async function CabinDetailPage({ params }: CabinDetailPageProps) {
  const { id } = await params;
  const cabin = await getCabin(id);

  return (
    <div>
      <h1>Cabin Details</h1>
      <p>Here are the details of the selected cabin.</p>
      <div style={{ marginTop: '1rem' }}>
        <h2>{cabin.name}</h2>
        <p>{cabin.description}</p>
        <p><strong>Location:</strong> {cabin.location}</p>
        <p><strong>Price per night:</strong> ${cabin.price}</p>
      </div>
    </div>
  );
}
Runs entirely on the server (no client fetch needed).
Next.js will pre-render the page (SSR or SSG).

-----------------------------------
Static Generation (build-time pre-rendering)
-----------------------------------
export async function generateStaticParams() {
  const res = await fetch('https://example.com/api/cabins');
  const cabins = await res.json();
  return cabins.map((cabin: any) => ({ id: cabin.id.toString() }));
}

export const revalidate = 600; // Incremental Static Regeneration

-----------------------------------
Notes
-----------------------------------
- `params` is now a Promise in Next.js 14.2+
-  Use async/await to unwrap it in your page component.
- Use generateStaticParams for static pre-rendering.
- Add revalidate to enable incremental static regeneration.
"""

pdf.set_font("Helvetica", "", 12)
pdf.multi_cell(0, 8, content)

# Save PDF
pdf.output("NextJS_Cabin_Detail_Guide.pdf")

print("✅ PDF generated: NextJS_Cabin_Detail_Guide.pdf")
