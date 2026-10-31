---
layout: default
title: Isoniazid
parent: Solo Predicción del Modelo (L5)
nav_order: 357
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Isoniazid: nueva indicación predicha, Conjuntivitis (nivel de evidencia L4). Indicación original: ISONIAZIDA"
monitor_inn: "isoniazid"
predicted_indications: ["conjunctivitis"]
---

# Isoniazid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Isoniazida: De Tuberculosis (Isoniazida) a Conjuntivitis
{: .text-alpha }

## Resumen en Una Frase

Isoniazida es un antibiótico antituberculoso, registrado en Colombia únicamente bajo el texto "ISONIAZIDA" como indicación.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis**, pero actualmente hay **0 ensayos clínicos** y solo **12 publicaciones** (en su mayoría reportes de caso, revisiones antiguas y artículos que describen la conjuntivitis como efecto adverso o manifestación asociada a BCG), por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ISONIAZIDA (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Conjuntivitis |
| Puntaje de Predicción TxGNN | 0.9936 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | al menos 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la isoniazida es un fármaco antituberculoso con actividad bactericida contra *Mycobacterium tuberculosis*, y su eficacia en tuberculosis está bien establecida.

El vínculo con la conjuntivitis es indirecto y limitado a una etiología específica: la queratoconjuntivitis flictenular, una reacción de hipersensibilidad a antígenos tuberculosos (y otros antígenos microbianos), y la rara tuberculosis conjuntival primaria. En estos casos, la isoniazida trata o previene la infección micobacteriana subyacente, no actúa directamente sobre la inflamación conjuntival.

No hay evidencia que respalde su eficacia en conjuntivitis bacteriana común, viral o alérgica. Varios artículos recuperados describen la conjuntivitis como efecto adverso o como manifestación de enfermedad reactiva asociada a BCG, no como objetivo terapéutico. El puntaje de 0.9936 es una predicción del modelo y no está respaldado por datos de ensayos clínicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohorte | Am Rev Respir Dis | Profilaxis con isoniazida en queratoconjuntivitis flictenular entre esquimales del suroeste de Alaska |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Revisión | Optom Clin | Efectos adversos oculares de fármacos sistémicos; la conjuntivitis aparece como efecto adverso de varios fármacos |
| [10084173](https://pubmed.ncbi.nlm.nih.gov/10084173/) | 1999 | Revisión | Rev Rhum (Engl Ed) | Poliartritis tras inmunoterapia intravesical con BCG; caso y revisión de 26 casos |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Reporte de caso | Medicine | Queratoconjuntivitis flictenular pediátrica asociada a tuberculosis sinonasal primaria |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Reporte de caso | Rev Rhum (Engl Ed) | Artropatía refractaria tras BCG intravesical; utilidad de la isoniazida |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Reporte de caso | Dtsch Med Wochenschr | Artritis reactiva crónica con conjuntivitis tras instilaciones de BCG |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Reporte de caso | Arch Ophthalmol | Tuberculosis primaria de la conjuntiva |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Serie de casos (tipo no clasificado) | Oftalmologia | 28 casos de queratoconjuntivitis tuberculosa, muchos en niños con tuberculosis primaria |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | No clasificado | Ann Ocul | Uso de isoniazida en el tratamiento local de la tuberculosis ocular |
| [8136810](https://pubmed.ncbi.nlm.nih.gov/8136810/) | 1993 | Serie de casos | Rev Rhum (Ed Fr) | Poliartritis en 4 pacientes tratados con BCG intravesical por carcinoma de vejiga |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190631 | GOTBISON® 100 MG. TABLETAS RECUBIERTAS (vigente) | Tableta recubierta | ISONIAZIDA |
| 20190638 | GOTBISON® 300 MG TABLETA RECUBIERTAS (vigente) | Tableta recubierta | ISONIAZIDA |
| 19927446 | SOLONEX® 100 MG TABLETAS (vigente) | Tableta | ISONIAZIDA |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento del modelo, no del prospecto)**: enfermedad o insuficiencia hepática (incluida insuficiencia hepática aguda), hepatitis, porfiria (incluida porfiria hereditaria y trastornos del metabolismo de porfirinas), enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, gota, enfermedad del sistema nervioso periférico y neuropatía periférica, abuso o dependencia de sustancias, y acetilación lenta.
- **Interacciones Farmacológicas**: se identificaron 242 interacciones. Entre las listadas:
  - Moderadas: acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, dapagliflozina, clorpropamida (fármacos antidiabéticos, con posible efecto sobre el control glucémico), metronidazol, alosetrón, budesonida, colecalciferol, calcifediol y calcitriol.
  - Menores: hidrocortisona, triamcinolona, dexametasona y betametasona.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L4), sin ensayos clínicos, y la literatura apoya únicamente un uso restringido a conjuntivitis de origen tuberculoso, no a conjuntivitis en general. Además, en Colombia no hay registros vigentes de isoniazida de componente único.

**Para avanzar se necesita:**
- Definir si la indicación de interés se limita a la queratoconjuntivitis flictenular o tuberculosis ocular, y no a la conjuntivitis en general
- Revisión sistemática de la literatura sobre isoniazida en tuberculosis ocular
- Datos del mecanismo de acción (MOA)
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones oficiales para el cribado de seguridad
- Evaluar la compatibilidad de vía de administración (la forma registrada es oral; no hay formulación oftálmica aprobada)
- Aclarar el estado regulatorio, dado que los tres registros están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

