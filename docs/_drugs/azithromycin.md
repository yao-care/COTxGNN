---
layout: default
title: Azithromycin
parent: Solo Predicción del Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
monitor_inn: "Azithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
last_modified_at: 2026-11-25
description: "Azithromycin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). Indicación original: AZITROMICINA"
---

# Azithromycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Azitromicina: antibiótico macrólido → síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Azitromicina es un antibiótico macrólido de uso oral con registros sanitarios en Colombia.
El modelo TxGNN predice que podría ser útil para el **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AZITROMICINA |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 8 de 10) |
| Número de Registros Sanitarios | 10 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Azithromycin (traducción no oficial): «La azitromicina es un fármaco antibacteriano macrólido. […] La azitromicina actúa uniéndose al ARNr 23S de la subunidad ribosómica 50S de los microorganismos sensibles, lo que inhibe la síntesis de proteínas bacterianas e impide el ensamblaje de la subunidad ribosómica 50S.» Texto original en inglés: "Azithromycin is a macrolide antibacterial drug. […] Azithromycin acts by binding to the 23S rRNA of the 50S ribosomal subunit of susceptible microorganisms inhibiting bacterial protein synthesis and impeding the assembly of the 50S ribosomal subunit." ([DailyMed: Zithromax (azithromycin dihydrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d24bacb-feff-4c6a-b8df-625e1435387a), versión del 2026-09-09; consultado el 2026-11-19). Por conocimiento general, es un macrólido con actividad antibacteriana y propiedades antiinflamatorias, pero esto no se ha vinculado a la hiperviscosidad policlonal.

Los datos compilados no sustentan ningún vínculo mecanístico entre el fármaco y esta enfermedad. El puntaje alto (0.9981) proviene únicamente del modelo de predicción y no está respaldado por ensayos ni literatura. La similitud con la indicación original aún está pendiente de evaluación.

Por ello, la predicción debe considerarse una hipótesis exploratoria, sin sustento clínico ni mecanístico demostrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19911014 | PENFLUZ 500 MG TABLETAS | TABLETA | AZITROMICINA | Vigente |
| 19970784 | AZITROFAR® TABLETAS | TABLETA | AZITROMICINA | Vigente |
| 19993382 | AZTROBAC 200 MG / 5 ML | POLVO ESTERIL PARA RECONSTITUIR A SUSPENSIONINYECTABLE | AZITROMICINA | Vigente |
| 20068317 | AKRIBACT® | TABLETA | AZITROMICINA | Vigente |
| 20099969 | MILAGRAM® TABLETAS | TABLETA | AZITROMICINA | Vigente |

Se muestran 5 de 10 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución registradas en los datos compilados (no provienen del texto del prospecto):** síndrome de QT largo (incluida la forma familiar), torsades de pointes, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, miastenia gravis (incluida la de inicio en adulto), enfermedad de la unión neuromuscular y trastornos de la audición o del sistema auditivo.
- **Interacciones farmacológicas:** los datos compilados solo muestran interacciones farmacológicas con el receptor de motilina (MLNR) y el receptor del gusto TAS2R4, sin nivel de gravedad clínica asignado.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe azitromicina en el síndrome de hiperviscosidad policlonal, y no hay un vínculo mecanístico respaldado; solo existe una predicción del modelo (nivel L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción de azitromicina para analizar un posible vínculo con la enfermedad
- Revisión de literatura biomédica y registros de ensayos específicos para esta enfermedad
- Evidencia preclínica que respalde una hipótesis mecanística
- Información de seguridad del prospecto, incluida la evaluación de las contraindicaciones señaladas (especialmente riesgo de prolongación del QT)

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zithromax (azithromycin dihydrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d24bacb-feff-4c6a-b8df-625e1435387a) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

