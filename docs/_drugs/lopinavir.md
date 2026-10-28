---
layout: default
title: Lopinavir
parent: Evidencia Moderada (L3-L4)
nav_order: 409
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-28
description: "Lopinavir: nueva indicación predicha, Infección por el virus de la inmunodeficiencia simia (SIV) (nivel de evidencia L4). Indicación original: Lopinavir y ritonavir"
monitor_inn: "LOPINAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Lopinavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Lopinavir: De Lopinavir y Ritonavir (infección por VIH) a Infección por el Virus de la Inmunodeficiencia Simia
{: .text-alpha }

## Resumen en Una Frase

Lopinavir es un inhibidor de la proteasa del VIH-1, registrado en Colombia en combinación con ritonavir. El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la inmunodeficiencia simia (SIV)**, con **0 ensayos clínicos** y **3 publicaciones** (todas en modelos animales primates) que respaldan de forma indirecta esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lopinavir y ritonavir |
| Nueva Indicación Predicha | Infección por el virus de la inmunodeficiencia simia (SIV) |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, lopinavir es un inhibidor de la proteasa del VIH-1 que se administra junto con ritonavir (que potencia sus niveles en sangre). Su eficacia frente al VIH-1 está establecida, y mecanísticamente podría ser aplicable al SIV.

El SIV es un lentivirus muy cercano al VIH, y su proteasa es estructuralmente similar. Por ello, es plausible que el mecanismo antiviral se traslade. Los tres estudios disponibles se realizaron en macacos: terapia antirretroviral cuádruple en macacos infectados con SIV, un virus quimérico SHIV con proteasa del VIH-1 en macacos rhesus, y terapia antirretroviral oral (incluido lopinavir/ritonavir) en monos infectados con SHIV.

Conviene tener presente que el SIV es una enfermedad de modelo animal/veterinaria, por lo que no existe una ruta de desarrollo clínico en humanos. Su valor principal es como modelo traslacional para el VIH, indicación para la cual lopinavir/ritonavir ya está aprobado. Las otras dos predicciones (síndrome de inmunodeficiencia adquirida felino y un trastorno del neurodesarrollo raro) tienen puntajes casi idénticos, que provienen del modelo TxGNN (aprendizaje profundo) y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, sobre todo en el segundo caso, donde no se identificó un vínculo mecanístico claro.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Estudio animal | Journal of Virology | Decaimiento viral rápido en macacos cynomolgus infectados con SIVmac251 que recibieron terapia antirretroviral cuádruple durante 7 días |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Estudio animal | Microbes and Infection | Construcción de un SHIV con gen de proteasa del VIH-1 que infecta macacos rhesus; útil para probar in vivo inhibidores de la proteasa |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Estudio animal | Journal of Virological Methods | Efecto de la terapia antirretroviral oral (AZT, 3TC y lopinavir/ritonavir) sobre el subconjunto CD8 en macacos con infección crónica por SHIV 89.6P |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20215036 (cancelado) | LOPARTA® 40MG/10MG | Gránulos | Lopinavir y ritonavir |
| 20115574 (cancelado) | LOPINAVIR 200 MG + RITONAVIR 50 MG | Tableta recubierta | Lopinavir y ritonavir |

---

## Consideraciones de Seguridad

No hay advertencias ni contraindicaciones de prospecto en los datos compilados. Se recomienda consultar el prospecto para esa información.

- **Contraindicaciones o condiciones de precaución según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, paro cardíaco súbito, enfermedad de conducción cardíaca, bloqueo auriculoventricular, cardiomiopatías, isquemia miocárdica y enfermedad coronaria; pancreatitis; enfermedad hepática, cirrosis, infección crónica por hepatitis B o C; enfermedad de la vesícula biliar; hiperglucemia, diabetes mellitus y cetoacidosis diabética; hipertrigliceridemia e hiperlipidemia familiar combinada; hiperbilirrubinemia y síndrome de Gilbert; deficiencia de potasio; hemofilia.
- **Interacciones farmacológicas**: se identificaron 65 interacciones; entre las principales de gravedad **mayor** están:
  - Dolasetrón
  - Papaverina

  Entre las de gravedad **moderada** se encuentran acarbosa, dapagliflozina, metformina, famotidina, levofloxacino, ondansetrón, palonosetrón y varios laxantes (bisacodilo, lactulosa, lactitol, hidróxido y citrato de magnesio, glicerina, aceite mineral, aceite de ricino, fenolftaleína). Cimetidina y clotrimazol se clasifican como **menores**.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a tres estudios preclínicos en primates no humanos, sin ensayos clínicos. Además, el SIV es una enfermedad de modelo animal sin ruta de desarrollo clínico en humanos, y el fármaco no tiene registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Definir si existe un objetivo de reposicionamiento relevante en humanos; el valor del SIV es como modelo traslacional del VIH, indicación ya aprobada.
- Datos detallados del mecanismo de acción.
- Advertencias y contraindicaciones del prospecto de INVIMA (actualmente un vacío bloqueante para el tamizaje de seguridad).
- Revisar si las predicciones con puntajes casi idénticos (síndrome de inmunodeficiencia adquirida felino y trastorno del neurodesarrollo) son artefactos del modelo; la segunda carece de vínculo mecanístico identificable.
- Aclarar la situación regulatoria: ambos registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

