---
layout: default
title: Enoxaparin
parent: Solo Predicción del Modelo (L5)
nav_order: 252
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Enoxaparin: nueva indicación predicha, Trombofilia por deficiencia de proteína C, autosómica recesiva (nivel de evidencia L5). Indicación original: ENOXAPARINA"
monitor_inn: "enoxaparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive"]
---

# Enoxaparin
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

## Enoxaparina: De Indicación Original (sin texto de indicación detallado) a Trombofilia por Deficiencia de Proteína C (Autosómica Recesiva)
{: .text-alpha }

## Resumen en Una Frase

Enoxaparina es una heparina de bajo peso molecular (anticoagulante) que en Colombia figura en sus registros sanitarios solo con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **trombofilia por deficiencia de proteína C, autosómica recesiva**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ENOXAPARINA (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general, la enoxaparina es una heparina de bajo peso molecular que potencia la acción de la antitrombina III e inhibe principalmente el factor Xa y, en menor grado, la trombina. Su eficacia como anticoagulante está bien establecida, aunque los registros colombianos no detallan la indicación aprobada.

En la deficiencia de proteína C se pierde la inactivación de los factores Va y VIIIa mediada por la proteína C activada, lo que genera un estado protrombótico. Por ello existe una lógica mecanística para usar un anticoagulante: la enoxaparina bloquea la cascada de coagulación por una vía distinta a la que está deficiente.

Esta justificación es plausible, pero se apoya en biología general de la anticoagulación. En las formas graves autosómicas recesivas (por ejemplo, la púrpura fulminante neonatal) el manejo habitual combina concentrado de proteína C y anticoagulación, y las heparinas se usan como parte del tratamiento. Los datos disponibles no permiten verificar ni graduar este uso. También es relevante el puente con heparina al iniciar antagonistas de la vitamina K, que en estos pacientes pueden causar necrosis cutánea por warfarina. El puntaje alto de TxGNN es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19960641 (cancelado) | ENOXPAR® INYECTABLE 60 MG /0.6 ML | Solución inyectable | ENOXAPARINA |
| 20084687 (cancelado) | ENOXAPARINA SÓDICA JERINGAS PRELLENADAS 60 MG/0.6 ML | Solución inyectable | ENOXAPARINA |

Ambos registros están cancelados, por lo que actualmente no hay productos vigentes con estos registros.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia la enoxaparina con contraindicación en las siguientes condiciones:
  - Hemorragia y trastornos de la coagulación: hemorragia intracraneal e intracerebral, enfermedad de la coagulación sanguínea, hemofilia, trombocitopenia, trombocitopenia inducida por heparina, trombastenia de Glanzmann, defecto cualitativo de plaquetas, deficiencia de antitrombina III, desprendimiento prematuro de placenta, enfermedad hematológica.
  - Hepáticas y biliares: insuficiencia hepática, enfermedad de las vías biliares, ictericia obstructiva.
  - Digestivas: úlcera péptica activa, colitis ulcerosa, enfermedad inflamatoria intestinal.
  - Cardiovasculares e infecciosas: endocarditis infecciosa (incluida la endocarditis bacteriana subaguda), arteriosclerosis obliterante.
  - Oculares: enfermedad de la retina, retinitis, retinopatía diabética, retinopatía hipertensiva, catarata diabética.
  - Óseas: osteoporosis y osteoporosis posmenopáusica.
- **Interacciones farmacológicas:** se identificaron 174 interacciones en total. Entre las de nivel **mayor** destacan:
  - Antiagregantes y antiinflamatorios: ácido acetilsalicílico, ibuprofeno, ketorolaco, abciximab.
  - Trombolíticos: alteplasa.
  - Oncológicos: acalabrutinib, trastuzumab emtansina, ibritumomab tiuxetán, tositumomab (incluido tositumomab I-131).
  - Otros: deferasirox.

  Entre las de nivel **moderado** figuran dexfenfluramina, fenfluramina, sibutramina, yoduro I-131, yoduro I-123, sugammadex, aliskiren, diclofenaco tópico y ketorolaco oftálmico.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5) y en un razonamiento mecanístico general, sin ensayos ni literatura para este par fármaco-enfermedad. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre heparinas de bajo peso molecular en deficiencia de proteína C (casos, series y guías).
- Datos del mecanismo de acción desde DrugBank.
- Descarga y análisis del prospecto de INVIMA para advertencias y contraindicaciones oficiales.
- Verificar la disponibilidad actual de enoxaparina en Colombia con registros vigentes.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original.
- Revisión de seguridad específica para pacientes pediátricos y neonatos, dado el perfil de la forma autosómica recesiva grave.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

