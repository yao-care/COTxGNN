---
layout: default
title: Ivermectin
parent: Solo Predicción del Modelo (L5)
nav_order: 363
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Ivermectin: nueva indicación predicha, Candidiasis vulvovaginal (nivel de evidencia L5). Indicación original: Ivermectina"
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "congenital candidiasis", "neonatal candidiasis", "candida glabrata", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
---

# Ivermectin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Ivermectina: De Ivermectina (indicación no detallada en el registro) a Candidiasis Vulvovaginal
{: .text-alpha }

## Resumen en Una Frase

Ivermectina es un antiparasitario de uso oral y tópico, comercializado en Colombia en solución oral y crema tópica; el registro sanitario solo consigna el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ivermectina (el registro INVIMA no detalla la indicación; el uso conocido es antiparasitario) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 5) |
| Número de Registros Sanitarios | 5 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la ivermectina actúa sobre los canales de cloruro activados por glutamato de los invertebrados, lo que explica su eficacia antiparasitaria. En humanos, los datos farmacológicos compilados la vinculan con el receptor de glicina, el receptor nicotínico de acetilcolina α7 y los receptores purinérgicos P2X4 y P2X7.

Los hongos carecen de los canales de cloruro activados por glutamato, por lo que no existe un mecanismo antifúngico establecido contra *Candida*. La relación entre la indicación original (infecciones parasitarias) y la nueva (candidiasis vulvovaginal) es débil: ambas son infecciones, pero con agentes y dianas muy distintos.

El puntaje alto de TxGNN (0.9995) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni de eficacia. Las demás predicciones del modelo (candidiasis esofágica, congénita, neonatal e invasiva, vulvovaginitis, VPH anogenital, vaginitis atrófica posmenopáusica) siguen el mismo patrón: sin ensayos y sin mecanismo plausible.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para candidiasis vulvovaginal.

Entre las otras predicciones, las dos publicaciones vinculadas no respaldan eficacia antifúngica. Ambas son reportes de caso sobre usos antiparasitarios:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Reporte de caso | BMJ Case Reports | Estrongiloidiasis diseminada tras tratamiento prolongado con corticoesteroides; no demuestra actividad contra candidiasis esofágica |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Reporte de caso | Australas J Dermatol | Dos niños inmunocomprometidos con sarna costrosa tratados con éxito con ivermectina oral; uno tenía candidiasis mucocutánea crónica, pero el resultado se refiere a la sarna |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20253293 | SIMPIOX | Solución oral | IVERMECTINA (vigente) |
| 19979253 | IVERMECTINA 0.6% GOTAS | Solución oral | IVERMECTINA (vigente) |
| 19980678 | QUANOX | Solución oral | IVERMECTINA (vigente) |
| 19938258 | KILOX 0.6% GOTAS | Solución oral | IVERMECTINA (vigente) |
| 20082013 | SOOLANTRA® 10 MG/G CREMA | Crema tópica | IVERMECTINA (vigente) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: loiasis y filariasis.
- **Interacciones farmacológicas / farmacología de dianas**: se identificaron 4 dianas humanas o de modelo animal: receptor de glicina (todos los subtipos), receptor nicotínico de acetilcolina α7, P2X4 (rata) y P2X7. No se dispone de niveles de gravedad.
- Se señalan además preocupaciones sobre la seguridad neonatal, con datos limitados, relevantes para las predicciones de candidiasis congénita y neonatal.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción corresponde únicamente a un modelo computacional (nivel L5), sin ensayos clínicos, sin literatura de apoyo y sin mecanismo antifúngico plausible. Además, el medicamento está comercializado en Colombia con 5 registros sanitarios vigentes, y la información de seguridad del prospecto no está disponible.

**Para avanzar se necesita:**
- Datos de mecanismo de acción detallados (consulta a DrugBank).
- Prospecto de INVIMA con advertencias y contraindicaciones, para el tamizaje de seguridad.
- Estudios preclínicos in vitro de actividad contra *Candida* que justifiquen continuar.
- Aclarar el estado regulatorio, dado que los 5 registros están cancelados, y la viabilidad de las vías de administración requeridas (por ejemplo, vaginal o tópica).
- Comparación con terapias ya aprobadas (azoles, equinocandinas), que son eficaces.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

