---
layout: default
title: Cetirizine
parent: Evidencia Alta (L1-L2)
nav_order: 147
evidence_level: L2
indication_count: 6
last_modified_at: 2026-10-14
description: "Cetirizine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L2). Indicación original: Cetirizina"
---

# Cetirizine
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **6** 
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

# Cetirizina: De Cetirizina (antihistamínico) a Urticaria Alérgica

## Resumen en Una Frase

Cetirizina es un antihistamínico de segunda generación, registrado originalmente en Colombia como cetirizina sola y en combinaciones para el resfriado común.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, con **1 ensayo clínico** (piloto de Fase 3) y **17 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cetirizina (indicación registrada en INVIMA, sin texto detallado) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la cetirizina es un antagonista selectivo del receptor de histamina H1 (la base de datos farmacológica la vincula con el gen HRH1). Se utiliza para controlar los síntomas de rinitis alérgica, urticaria crónica y asma inducida por polen, y tiene una penetración cerebral mínima, por lo que causa poca somnolencia.

En la urticaria, la liberación de histamina por los mastocitos produce la reacción de roncha y eritema. El bloqueo H1 actúa directamente sobre esta fisiopatología. Los antihistamínicos ya son tratamiento de primera línea respaldado por guías en urticaria, por lo que esta predicción se acerca más a un uso establecido que a un reposicionamiento novedoso. La pregunta clínica se centra sobre todo en la vía (intravenosa) y el contexto (presentación aguda), no en el mecanismo.

Otras predicciones del modelo con distinto grado de respaldo: urticaria por frío (puntaje 99.95%, nivel L3, con estudios clínicos pequeños y un estudio experimental), enfermedad de la cavidad nasal (99.77%, L4, término demasiado amplio), laringofaringitis aguda, conjuntivitis por rosácea y dermatitis atópica recalcitrante (todas L5, solo predicción del modelo, con mecanismo poco plausible).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Fase 3 (piloto) | Completado | 36 | Estudio piloto multicéntrico, doble ciego y aleatorizado de cetirizina intravenosa 10 mg frente a difenhidramina intravenosa 50 mg en urticaria aguda, para evaluar la viabilidad de un ensayo de Fase 3. No fue diseñado para demostrar eficacia. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Revisión | Drugs | Reevaluación de cetirizina: antihistamínico H1 específico y de acción prolongada, eficaz y bien tolerado en rinitis alérgica y urticaria idiopática crónica en adultos. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Revisión | Drugs | Propiedades farmacológicas y potencial clínico de cetirizina en rinitis alérgica, asma por polen y urticaria crónica; sin efecto depresor central a 10 mg diarios. |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Revisión | Drugs | Los antihistamínicos no sedantes son la base del tratamiento de la urticaria idiopática crónica. |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Revisión | Allergy | Estudios clínicos con cetirizina en rinitis alérgica y urticaria crónica (sin resumen disponible). |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Revisión | Ann Pharmacother | Eficacia y seguridad de antihistamínicos orales de primera y nueva generación en rinitis alérgica y urticaria idiopática crónica. |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Revisión | Allergy Asthma Proc | Levocetirizina (enantiómero R de cetirizina) en rinitis alérgica y urticaria idiopática crónica. |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Revisión | Clin Ther | Levocetirizina en rinitis alérgica y urticaria idiopática crónica en adultos y niños. |
| [17017922](https://pubmed.ncbi.nlm.nih.gov/17017922/) | 2006 | Revisión | Curr Med Chem | Actualización de levocetirizina: alta biodisponibilidad, inicio rápido y mínimo metabolismo hepático. |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Revisión | Clin Allergy Immunol | Antihistamínicos H1 en niños: evidencia de nivel 1 en rinoconjuntivitis alérgica. |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Reporte de caso | J Clin Gastroenterol | Caso de colestasis inducida por cetirizina en un hombre de 28 años (señal de seguridad hepática). |

*Nota: de las 17 publicaciones disponibles se listan 10. Varias tratan de otros antihistamínicos (fexofenadina, bilastina, rupatadina, ebastina) y aportan solo apoyo indirecto.*

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20149297 | CETISWISS (cancelado) | Cápsula blanda | CETIRIZINA |
| 20152795 | PARAGRIP CAPSULAS (cancelado) | Cápsula dura | PREPARACIONES DE OTRAS COMBINACIONES PARA EL RESFRIADO COMÚN |
| 20113482 | ONEGRIP® (cancelado) | Cápsula dura | PARACETAMOL COMBINACIONES EXCLUYENDO SICOLEPTICOS |

Los tres registros están cancelados; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia la cetirizina con enfermedades como hipertensión, enfermedad renal (incluida insuficiencia renal crónica y terminal), enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, enfermedad coronaria y aterosclerosis, glaucoma de ángulo cerrado e hipertiroidismo (enfermedad de Graves, tirotoxicosis). Deben verificarse contra el prospecto oficial.
- **Señal hepática en la literatura:** existe un reporte de caso de colestasis inducida por cetirizina; en ensayos clínicos se observaron elevaciones transitorias y reversibles de transaminasas en menos del 2% de los pacientes.
- **Interacciones farmacológicas:** no se registraron interacciones medicamentosas formales; solo se identificó la unión al receptor H1 como blanco farmacológico.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo (bloqueo H1) es directo y plausible, y los antihistamínicos ya son tratamiento de primera línea en urticaria. La evidencia específica se limita a un piloto de Fase 3 (n=36) sobre la formulación intravenosa, sin un ECA de Fase 3 definitivo (nivel L2). Además, en Colombia no hay registros vigentes.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) y confirmar los datos del mecanismo de acción.
- Un ensayo de Fase 3 definitivo que compare la cetirizina intravenosa con el tratamiento estándar en urticaria aguda.
- Verificar las contraindicaciones del grafo de conocimiento (renal, hepática, cardiovascular, glaucoma, próstata) frente al prospecto.
- Definir la situación regulatoria: un nuevo registro o la reactivación, y la vía de administración (intravenosa) en Colombia.
- Para indicaciones de menor evidencia (cavidad nasal, laringofaringitis, conjuntivitis por rosácea, dermatitis atópica recalcitrante), mantener en espera hasta contar con estudios reales y acotar la definición de la enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

