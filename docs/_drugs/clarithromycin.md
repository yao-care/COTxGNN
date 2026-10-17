---
layout: default
title: Clarithromycin
parent: Solo Predicción del Modelo (L5)
nav_order: 162
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Clarithromycin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Claritromicina"
monitor_inn: "Clarithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
---

# Clarithromycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Claritromicina: De Indicación Registrada (Claritromicina) a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Claritromicina es un antibiótico macrólido que contó con registros sanitarios en Colombia (productos Klaricid®), actualmente cancelados.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Claritromicina (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la claritromicina es un antibiótico macrólido con efectos inmunomoduladores (supresión de citocinas proinflamatorias). Su eficacia como antibacteriano está bien establecida, pero mecanísticamente su aplicabilidad al síndrome de hiperviscosidad policlonal no es clara.

La hiperviscosidad policlonal se origina por un exceso de inmunoglobulinas, por ejemplo en enfermedades autoinmunes o infecciones crónicas. No existe evidencia de que la claritromicina modifique los niveles de inmunoglobulinas ni la viscosidad sérica.

Por lo tanto, el puntaje alto de TxGNN (0.993) debe interpretarse con cautela: es una predicción basada en el grafo de conocimiento y no está respaldada por estudios reales.

### Otras indicaciones predichas (referencia)

| Rango | Enfermedad | Puntaje TxGNN | Evidencia | Comentario |
|---|---|---|---|---|
| 2 | Hiperamilasemia | 99.35% | L4 | Un reporte de caso (infección por *M. abscessus* con macroamilasemia); coexistencia incidental, sin evidencia de eficacia |
| 3 | Analbuminemia congénita | 99.21% | L5 | Sin mecanismo plausible (trastorno genético del gen ALB) |
| 4 | Queratoconjuntivitis epitelial punteada | 99.11% | L4 | Vínculo indirecto plausible (macrólidos en disfunción de glándulas de Meibomio); pregunta de investigación |
| 5 | Incompatibilidad de grupo sanguíneo | 99.07% | L5 | Sin mecanismo plausible |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de hiperviscosidad policlonal.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20179259 | KLARICID® SUSPENSION 125 MG/ 5 ML | Gránulos | Claritromicina | Cancelado |
| 20086452 | KLARICID® UD | Tableta de liberación modificada | Claritromicina | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** síndrome de QT largo, torsades de pointes, taquicardia ventricular, insuficiencia y enfermedad hepática, colestasis, porfirias, enfermedad renal, miastenia gravis, colitis por *Clostridium difficile*, osteoporosis, fractura ósea, enfermedad de la vesícula biliar, mononucleosis infecciosa y otras condiciones relacionadas.
- **Interacciones farmacológicas** (se identificaron 100 en total; se muestran algunas de las principales):
  - **Mayores:** abemaciclib, fentanilo, acalabrutinib.
  - **Moderadas:** paclitaxel, tramadol, nifedipino, famotidina, formoterol, adenosina, afatinib, etinilestradiol, hidrocortisona, acarbosa, abiraterona, trastuzumab emtansina, flunisolida.
  - **Menores:** dolutegravir, zidovudina, loratadina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de hiperviscosidad policlonal carece de ensayos clínicos, de literatura y de un vínculo mecanístico claro (nivel L5). Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la claritromicina.
- Prospecto oficial de INVIMA con advertencias y contraindicaciones.
- Estudios preclínicos que evalúen un efecto sobre inmunoglobulinas o viscosidad sérica.
- Evaluar de forma prioritaria la queratoconjuntivitis epitelial punteada (rango 4), que tiene un vínculo indirecto plausible, como pregunta de investigación.
- Aclarar la situación regulatoria (registros cancelados) antes de cualquier desarrollo local.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

