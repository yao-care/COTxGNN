---
layout: default
title: Iohexol
parent: Solo Predicción del Modelo (L5)
nav_order: 352
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Iohexol: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: IOHEXOL"
monitor_inn: "IOHEXOL"
predicted_indications: ["insomnia (disease)", "anxiety"]
---

# Iohexol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Iohexol: De Medio de Contraste Radiológico a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Iohexol es un medio de contraste yodado no iónico, utilizado en estudios de imagen radiológica; en el registro sanitario colombiano su indicación aparece simplemente como "IOHEXOL".
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero no existen **ensayos clínicos** ni **publicaciones** que respalden esta dirección.
La predicción se considera un artefacto del modelo, sin evidencia real que la sustente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IOHEXOL (el registro no detalla una indicación clínica; corresponde a un medio de contraste radiológico) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Iohexol (traducción no oficial): «Los átomos de yodo del iohexol atenúan los rayos X en proporción directa a la concentración de iohexol. Dado que la concentración varía con el tiempo, el iohexol proporciona un contraste de imagen dependiente del tiempo que puede ayudar a visualizar las estructuras corporales.» Texto original en inglés: "The iodine atoms in iohexol provide attenuation of X-rays in direct proportion to the concentration of iohexol. Since concentration changes over time, iohexol provides time-dependent image contrast which may assist in visualizing body structures." ([DailyMed: Omnipaque (iohexol) prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=508c42eb-f5e5-44f1-e063-6294a90a4d1f), versión del 2026-04-28; consultado el 2026-11-19). Según la información conocida, iohexol es un medio de contraste yodado no iónico, farmacológicamente inerte, que se utiliza para visualizar estructuras en estudios radiológicos y no actúa sobre dianas del sistema nervioso central.

No se identifica una relación plausible entre su uso original (imagenología diagnóstica) y el tratamiento del insomnio. No existe un mecanismo conocido por el cual un agente de contraste pueda intervenir en la regulación del sueño.

El puntaje muy alto del modelo (0.9987) parece ser un artefacto del modelo TxGNN (aprendizaje profundo): no hay mecanismo plausible, ensayos clínicos ni literatura de apoyo. Por ello, la predicción debe tomarse con mucha cautela.

**Otra predicción del modelo: ansiedad (puntaje 0.9925).** Tampoco existe un vínculo farmacológico creíble. La literatura recuperada menciona la ansiedad solo como contexto del procedimiento o como efecto adverso (por ejemplo, tras mielografía), no como un resultado terapéutico. Su nivel de evidencia también es L5 y la recomendación es Hold.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para insomnio.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para insomnio.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20139023 | IOHEXOL INYECCION300MG/ML | SOLUCION INYECTABLE | IOHEXOL | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

El fabricante del único registro es Unique Pharmaceutical Laboratories.

<!-- review:begin co-lic-20261105-iohexol-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El fabricante del único registro es Unique Pharmaceutical Laboratories. No hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-iohexol-1 -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se identificaron 100 interacciones en total. Entre las revisadas, la gran mayoría son de nivel **Mayor** y una de nivel Moderado (manitol). Las principales son:
  - Corticosteroides: hidrocortisona, dexametasona, betametasona, triamcinolona
  - Metformina
  - Anfotericina B (incluida la formulación de complejo lipídico)
  - Aminoglucósidos y glucopéptidos: kanamicina, neomicina, vancomicina
  - Levofloxacino
  - Mesalazina y balsalazida
  - Bupropión, dietilpropión y fentermina
  - Morfina, dronabinol y metoclopramida

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica ni literatura que respalde el uso de iohexol en insomnio, y no hay un mecanismo farmacológico plausible. El puntaje alto del modelo TxGNN (aprendizaje profundo) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, y el único registro sanitario en Colombia está vigente (1 licencia válida de 1).

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica creíble que vincule el fármaco con el sueño
- Estudios preclínicos que demuestren algún efecto sobre el sistema nervioso central
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) para completar el análisis de seguridad
- Reevaluar la utilidad de la predicción antes de destinar recursos adicionales

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "No hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Omnipaque (iohexol) prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=508c42eb-f5e5-44f1-e063-6294a90a4d1f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

