---
layout: default
title: Carvedilol
parent: Solo Predicción del Modelo (L5)
nav_order: 139
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Carvedilol: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L5). Indicación original: Carvedilol"
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Carvedilol
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

# Carvedilol: De Indicación Registrada (Carvedilol) a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Carvedilol es un betabloqueante no selectivo con actividad bloqueadora alfa-1, registrado en Colombia como medicamento de un solo principio activo (tabletas), cuyos dos registros sanitarios están actualmente cancelados.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación específica.
La predicción es solo computacional (nivel de evidencia L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carvedilol (el registro sanitario no detalla la indicación; solo repite el nombre del fármaco) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (0 vigentes, 2 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, carvedilol es un betabloqueante no selectivo con actividad bloqueadora alfa-1, y su eficacia en hipertensión e insuficiencia cardíaca está bien establecida en la práctica clínica. Mecanísticamente, podría ser aplicable a formas graves de hipertensión por su efecto vasodilatador.

La hipertensión renovascular maligna depende en gran medida de la activación del sistema renina-angiotensina. El betabloqueo de carvedilol reduce la liberación de renina, lo que ofrece solo un apoyo indirecto. El bloqueo alfa-1 aporta vasodilatación, pero no hay estudios específicos en esta indicación.

Cabe señalar que el puntaje TxGNN es idéntico al de la enfermedad renal hipertensiva maligna (segunda predicción), lo que sugiere una vecindad compartida en el grafo de conocimiento y no evidencia independiente. Por ello, el puntaje alto no debe interpretarse como respaldo clínico.

### Otras predicciones del modelo

| Posición | Indicación Predicha | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|------|
| 2 | Enfermedad renal hipertensiva maligna | 99.55% | L5 | Hold |
| 3 | Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.54% | L5 | Hold |
| 4 | Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.54% | L4 | Pregunta de investigación |
| 5 | Síndrome de Braddock | 99.37% | L5 | Hold |

Sobre la hipertensión pulmonar: los betabloqueantes se usan con cautela por el posible deterioro de la función del ventrículo derecho, y la tolerabilidad respiratoria del betabloqueo no selectivo en enfermedad pulmonar es una preocupación de seguridad. En el síndrome de Braddock no se pudo establecer un vínculo mecanístico claro.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para hipertensión renovascular maligna.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

Para la cuarta predicción (hipertensión pulmonar por enfermedad pulmonar y/o hipoxia) se recuperaron publicaciones con apoyo únicamente indirecto y preclínico. Las más relevantes:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26291659](https://pubmed.ncbi.nlm.nih.gov/26291659/) | 2015 | Estudio animal (rata) | Eur J Pharmacol | Carvedilol revirtió la hipertensión inducida por hipoxia intermitente crónica; es hipertensión sistémica, no pulmonar |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Revisión | Cardiovasc Drugs Ther | Efectos respiratorios de los betabloqueantes en insuficiencia cardíaca; el concepto de contraindicación en función pulmonar alterada se ha cuestionado |
| [16639551](https://pubmed.ncbi.nlm.nih.gov/16639551/) | 2006 | Estudio preclínico | Pflugers Arch | Carvedilol inhibió la hipertrofia ventricular derecha inducida por hipoxia hipobárica crónica |
| [20508210](https://pubmed.ncbi.nlm.nih.gov/20508210/) | 2010 | Estudio animal (rata) | Am J Respir Crit Care Med | El bloqueo adrenérgico revirtió la remodelación y disfunción del corazón derecho en ratas con hipertensión pulmonar |
| [24798657](https://pubmed.ncbi.nlm.nih.gov/24798657/) | 2014 | Estudio cruzado (11 pacientes) | J Clin Hypertens | Comparó carvedilol 20 mg vs nifedipino 40 mg nocturnos sobre la presión arterial durante el sueño en hipertensos con apnea del sueño |
| [10862260](https://pubmed.ncbi.nlm.nih.gov/10862260/) | 2000 | Revisión | Presse Med | Intoxicación por betabloqueantes; carvedilol figura entre los más tóxicos |

Varias de las publicaciones recuperadas no guardan relación con la indicación (derivados indólicos, colangiocarcinoma, cáncer de mama triple negativo, melanoma uveal).

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 218019 | DILATREND TABLETAS 6.25MG (CHEPLAPHARM ARZNEIMITTEL GMBH) | Tableta | Carvedilol | Cancelado |
| 19969274 | CARVEDILOL 25 MG TABLETAS RECUBIERTAS (LABORATORIOS LA SANTE S.A.) | Tableta recubierta | Carvedilol | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto del prospecto): insuficiencia hepática, bronquitis, asma (incluidas las formas intrínseca y alérgica), diabetes mellitus, cetoacidosis diabética, trastornos hipotensivos, enfermedad vascular periférica, claudicación intermitente, enfermedad arterial periférica, bloqueo auriculoventricular, enfisema pulmonar, enfermedad bronquial, angina de Prinzmetal, síndrome del seno enfermo (incluida su forma familiar), anafilaxia y síndrome del iris flácido intraoperatorio.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; las principales son:
  - **Mayor**: epinefrina.
  - **Moderada**: hidrocortisona, hioscina (hiosciamina), bupropión, triamcinolona, morfina, atropina, dexametasona, lorcaserina, betametasona, budesonida, canagliflozina, acetohexamida, y sales de calcio (fosfato, acetato, carbonato, citrato).
  - **Menor**: ácido acetilsalicílico, hidróxido de aluminio, attapulgita.
- **Preocupación específica**: la tolerabilidad respiratoria del betabloqueo no selectivo en pacientes con enfermedad pulmonar (relevante para las predicciones de hipertensión pulmonar) y el uso cauteloso en hipertensión pulmonar por posible deterioro del ventrículo derecho.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura para hipertensión renovascular maligna. Además, ambos registros sanitarios en Colombia están cancelados, y el vínculo mecanístico (reducción de renina por betabloqueo) es solo indirecto.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente no disponible.
- Obtener datos del mecanismo de acción desde DrugBank.
- Revisar sistemáticamente la literatura clínica sobre betabloqueantes/carvedilol en hipertensión renovascular maligna y nefropatía hipertensiva.
- Aclarar el estado regulatorio: confirmar si existe algún registro vigente o si se requeriría un nuevo trámite ante INVIMA.
- Evaluar la seguridad en poblaciones con enfermedad respiratoria o pulmonar antes de considerar cualquier indicación de hipertensión pulmonar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

