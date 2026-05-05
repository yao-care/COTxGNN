---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

El skill confirma que estoy en el contexto correcto del TxGNN pipeline. Ahora genero el informe completo a partir del Evidence Pack proporcionado.

---

# Ertapenem: De Infecciones Bacterianas Complicadas a Artritis Bacteriana

## Resumen en Una Frase

Ertapenem es un antibiótico carbapenem de amplio espectro, aprobado internacionalmente para el tratamiento de infecciones bacterianas complicadas (intraabdominales, cutáneas, neumonía adquirida en comunidad e infecciones urinarias), aunque actualmente no se encuentra comercializado en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Artritis Bacteriana (Artritis Séptica)**,
con **0 ensayos clínicos** y **10 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas complicadas (referencia internacional; sin registro en Colombia) |
| Nueva Indicación Predicha | Artritis Bacteriana |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Sin embargo, según la información conocida, ertapenem es un carbapenem de clase 1-beta-metil que se une preferentemente a las proteínas fijadoras de penicilina (PBP) 2 y 3, inhibiendo la síntesis de la pared bacteriana. Su espectro de actividad incluye potentes efectos contra bacilos gramnegativos como *Klebsiella pneumoniae*, *Prevotella bivia*, *Citrobacter koseri* y *Clostridium* spp., todos ellos microorganismos documentados como causantes de artritis séptica, especialmente en pacientes inmunocomprometidos, diabéticos o con comorbilidades.

La artritis bacteriana comparte una base microbiológica parcialmente superpuesta con las indicaciones originales de ertapenem: los mismos patógenos gramnegativos que causan infecciones intraabdominales y complicaciones de pie diabético pueden ser agentes etiológicos de artritis séptica. La propiedad de dosificación una vez al día de ertapenem lo hace especialmente adecuado para la Terapia Antimicrobiana Parenteral Ambulatoria (OPAT), modalidad clínicamente relevante para tratamientos prolongados de infecciones óseas y articulares cuando no es posible la cirugía definitiva.

No obstante, existe una limitación estructural importante: *Staphylococcus aureus*, el patógeno más frecuente en artritis séptica, no está cubierto de forma eficaz por ertapenem en monoterapia. Esta condición restringe su aplicabilidad clínica a los casos confirmados por cultivo con patógenos gramnegativos susceptibles, y hace indispensable la guía microbiológica para la selección del antibiótico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Reporte de Caso | J Chemotherapy | Artritis séptica de muñeca por *Klebsiella pneumoniae* tratada exitosamente con ertapenem más levofloxacina |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Reporte de Caso | BMJ Case Reports | *Citrobacter koseri* causando artritis séptica con osteomielitis en pie diabético; tratamiento exitoso con ertapenem |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Reporte de Caso | Anaerobe | Primer caso reportado de artritis séptica nativa de hombro y osteomielitis por *Clostridium paraputrificum*; manejo con ertapenem |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Reporte de Caso | J Investig Med High Impact Case Rep | Artritis séptica por *Prevotella bivia* en adulto inmunocompetente; ertapenem como opción terapéutica para anaerobios gramnegativos |
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohorte Retrospectiva | Antimicrob Agents Chemother | Seguridad y eficacia de ertapenem ambulatorio (OPAT) a largo plazo en 306 pacientes; incluye infecciones óseas y articulares entre las indicaciones más comunes |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohorte Retrospectiva | J Antimicrob Chemother | Terapia antibiótica supresora subcutánea para infecciones óseas y articulares en 10 pacientes; ertapenem como β-lactámico de referencia en terapia supresora prolongada |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Descriptivo Retrospectivo | Clin Lab | Distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en niños menores de 4 años; contexto microbiológico relevante |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Cohorte Comparativa | J Antimicrob Chemother | Evaluación de temocillin como alternativa a carbapenems (incluyendo ertapenem) en infecciones óseas por Enterobacterales resistentes a cefalosporinas de 3.ª generación |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro / Básico | Diagn Microbiol Infect Dis | Auranofin restaura la susceptibilidad de ertapenem frente a *E. coli* resistente a carbapenems; potencial de terapia combinada |
| [29183082](https://pubmed.ncbi.nlm.nih.gov/29183082/) | 2017 | Revisión | JAMA | Avances en diagnóstico y tratamiento de hidradenitis supurativa; relevancia indirecta como infección bacteriana cutánea profunda con manejo antibiótico similar |

---

## Información de Mercado en Colombia

Ertapenem **no se encuentra comercializado en Colombia**. La consulta a la base de datos de INVIMA no arrojó registros sanitarios activos para este medicamento. No existe, por tanto, una indicación aprobada local de referencia.

A modo de contexto internacional, ertapenem (marca Invanz®) cuenta con aprobación en múltiples países para infecciones intraabdominales complicadas, infecciones de piel y tejidos blandos (incluidas las del pie diabético), neumonía adquirida en la comunidad, infecciones del tracto urinario complicadas e infecciones pélvicas agudas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia actual (L3) se limita a reportes de caso y cohortes retrospectivas pequeñas, sin ningún ensayo clínico prospectivo que evalúe ertapenem específicamente para artritis bacteriana. La ausencia de comercialización en Colombia y la cobertura insuficiente frente a *S. aureus* —patógeno predominante en esta indicación— representan barreras de entrada significativas que no permiten avanzar sin evidencia adicional.

**Para avanzar se necesita:**
- Datos completos del mecanismo de acción (MOA) de ertapenem desde DrugBank
- Información de advertencias y contraindicaciones del prospecto oficial (actualmente con brecha de datos)
- Estudios prospectivos o ensayo clínico de Fase 2 enfocado en artritis séptica por gramnegativos susceptibles
- Perfil de penetración ósea y articular documentado (estudios farmacocinéticos/farmacodinámicos)
- Evaluación de viabilidad de registro sanitario en Colombia para habilitar el mercado
- Definición de criterio de selección de pacientes basado en cultivo microbiológico (patógeno gramnegativo confirmado)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

