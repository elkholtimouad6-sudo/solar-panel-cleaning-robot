#!/usr/bin/env python3
"""
Script de génération PDF - TIPE Presentation
Convertit la présentation HTML en PDF professionnel
"""

# Installation requise: pip install weasyprint pillow

from weasyprint import HTML, CSS
from pathlib import Path
import os

def generate_pdf():
    """Génère le PDF à partir du HTML"""
    
    # Chemin du fichier HTML
    html_file = "PRESENTATION.html"
    pdf_output = "TIPE_Robot_Nettoyage_Panneaux_Solaires.pdf"
    
    # CSS personnalisé pour impression
    css_print = CSS(string="""
        @page {
            size: A4;
            margin: 1cm;
            @bottom-center {
                content: "Page " counter(page) " / " counter(pages);
                font-size: 10px;
            }
        }
        
        body {
            font-family: 'Segoe UI', sans-serif;
            line-height: 1.6;
        }
        
        nav {
            display: none;  /* Cache la navigation */
        }
        
        section {
            page-break-inside: avoid;
            margin-bottom: 20px;
        }
        
        h2 {
            page-break-after: avoid;
            margin-top: 20px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        pre {
            font-size: 9px;
            overflow: hidden;
        }
    """)
    
    try:
        # Conversion HTML → PDF
        HTML(html_file).write_pdf(
            pdf_output,
            stylesheets=[css_print],
            zoom=1.0
        )
        
        print(f"✅ PDF généré avec succès: {pdf_output}")
        print(f"📊 Taille: {os.path.getsize(pdf_output) / 1024 / 1024:.2f} MB")
        
    except Exception as e:
        print(f"❌ Erreur lors de la génération du PDF: {e}")
        print("\n📌 Solution: Installer weasyprint")
        print("   pip install weasyprint pillow")

if __name__ == "__main__":
    generate_pdf()
