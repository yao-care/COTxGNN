---
layout: default
title: Imipenem
parent: Solo Predicción del Modelo (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Imipenem
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Imipenem: De Imipenem y Cilastatina a Esclerodermia Difusa

## Resumen en Una Frase

Imipenem es un antibiótico carbapenémico que en Colombia se registró en combinación con cilastatina (presentación inyectable). El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Entre las indicaciones evaluadas, la más respaldada es la **infección por *Staphylococcus aureus*** (2 ensayos clínicos de Fase 4 y 20 publicaciones), aunque con evidencia limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Imipenem y cilastatina |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, imipenem es un carbapenémico que inhibe la síntesis de la pared celular bacteriana, y se administra junto con cilastatina, que evita su degradación renal. Su eficacia en infecciones bacterianas graves está establecida.

Para la esclerodermia difusa, **no se identifica un vínculo mecanístico plausible**: es una enfermedad autoinmune y fibrótica, y un antibiótico que actúa sobre la pared bacteriana no tiene un blanco conocido en ese proceso. El puntaje tan alto del modelo es una predicción basada en el grafo de conocimiento, sin respaldo de ensayos ni literatura.

Otras predicciones del modelo sí tienen una lógica antibacteriana más coherente, aunque con evidencia indirecta:
- **Fiebre tifoidea, paratifoidea y salmonelosis:** imipenem tiene actividad contra enterobacterias, y los carbapenémicos se usan como última opción en cepas de *Salmonella* Typhi extensamente resistentes. La literatura es sobre todo de vigilancia de susceptibilidad, sin datos clínicos controlados.
- **Infección por *S. aureus*:** es la indicación con más evidencia (nivel L3). Imipenem se ha estudiado principalmente en combinación (por ejemplo, con fosfomicina) para SARM; no es apropiado como monoterapia en SARM.
- **Sinusitis y rinosinusitis crónica:** la literatura trata de bacteriología y otros antibióticos, no de imipenem. Usar un carbapenémico en estos casos entraría en conflicto con los principios de uso racional de antimicrobianos.
- **Neoplasia de senos paranasales y síndrome de eosinofilia-mialgia:** sin vínculo mecanístico.

---

## Evidencia de Ensayos Clínicos

Para la esclerodermia difusa no hay ensayos clínicos registrados. Los únicos ensayos disponibles corresponden a la indicación alternativa de mayor evidencia, la infección por *S. aureus*:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Fase 4 | Completado | 50 | Fosfomicina más imipenem frente a vancomicina (tratamiento estándar) en endocarditis infecciosa por SARM |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Fase 4 | Desconocido | 60 | Linezolid solo o combinado con un carbapenémico contra SARM en neumonía asociada a ventilador; el carbapenémico no es necesariamente imipenem |

---

## Evidencia de Literatura

Para la esclerodermia difusa no hay literatura disponible. Las publicaciones más relevantes se encuentran en otras indicaciones predichas:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Estudio clínico | Antimicrob Agents Chemother | Imipenem-cilastatina evaluado en 23 pacientes con infecciones por *S. aureus* sensible y resistente a meticilina |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Reporte de caso (comentario) | Antimicrob Agents Chemother | Combinación imipenem/cilastatina más fosfomicina en infección refractaria por SARM |
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Estudio observacional | Cureus | Carbapenémicos como última línea en fiebre tifoidea por cepas MDR y XDR |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Reporte de caso | J Med Liban | Rabdomiólisis e insuficiencia renal por *Salmonella* Typhi tratadas con imipenem/cilastatina y hemodiálisis |
| [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/) | 2011 | In vitro | JPMA | Concentraciones inhibitorias mínimas de imipenem y otros antibióticos frente a *Salmonella* Typhi y Paratyphi |
| [3469191](https://pubmed.ncbi.nlm.nih.gov/3469191/) | 1986 | Evaluación clínica | J Antimicrob Chemother | Imipenem/cilastatina en 35 pacientes con infecciones nosocomiales y patógenos multirresistentes |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Estudio animal | J Antimicrob Chemother | Imipenem en endocarditis experimental por *S. aureus* en conejos |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | Estudio in vitro/in vivo | J Antimicrob Chemother | Efecto sinérgico de vancomicina más imipenem contra SARM |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19982795 | Imipenem y cilastatina 1 g (Farmalógica S.A.) | Polvo estéril para reconstituir a solución inyectable | Imipenem y cilastatina |
| 20256282 | Imipenem + cilastatina 500 + 500 mg (Holland Group S.A.S) | Polvo estéril para reconstituir a solución inyectable | Imipenem y cilastatina |
| 20072860 | Imipenem 500 mg cilastatina 500 mg (Vicarfarmacéutica S.A.) | Polvo estéril para reconstituir a solución inyectable | Imipenem y cilastatina |

Los tres registros figuran como cancelados, por lo que actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no provienen del prospecto): epilepsia, enfermedad renal, piouréter, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas** (15 identificadas):
  - **Mayores:** bupropión, iohexol, iopamidol.
  - **Moderadas:** polietilenglicol (3350 con electrolitos), dicumarol, warfarina, lindano, aminofilina, dyphylline, oxtrifilina, teofilina, ciclosporina, etinilestradiol, ácido micofenólico y pemetrexed.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para la indicación principal predicha (esclerodermia difusa) no existe vínculo mecanístico plausible ni evidencia clínica o bibliográfica; el puntaje del modelo es solo una predicción basada en el grafo. Además, no hay registros sanitarios vigentes en Colombia, y las indicaciones antibacterianas con más sentido (tifoidea, *S. aureus*) ya cuentan con alternativas establecidas o requieren combinaciones.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto y los datos del mecanismo de acción.
- Si se desea explorar una alternativa, priorizar la infección por *S. aureus* (SARM) en combinación con fosfomicina, o la fiebre tifoidea por cepas extensamente resistentes, con una revisión sistemática de la evidencia existente.
- Verificar la situación regulatoria, dado que todos los registros están cancelados.
- Evaluar la compatibilidad de vía de administración y la relación con la indicación original, que quedan pendientes.
- Considerar los principios de uso racional de antimicrobianos antes de proponer cualquier uso de un carbapenémico en sinusitis o rinosinusitis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

