---
layout: default
title: Misoprostol
parent: Solo Predicción del Modelo (L5)
nav_order: 288
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Misoprostol: De Indicación No Especificada a Amenorrea

## Resumen en Una Frase

Los datos disponibles no registran la indicación original de Misoprostol; solo se sabe que está comercializado en Colombia como tableta oral de 200 mcg.
El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, pero hay **0 ensayos clínicos** y **7 publicaciones** relacionadas de forma indirecta.
Ninguna de esas publicaciones estudia Misoprostol como tratamiento de la amenorrea, por lo que la predicción no tiene respaldo clínico directo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro sanitario solo repite el nombre "Misoprostol") |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, Misoprostol es un análogo sintético de la prostaglandina E1 que provoca contracciones uterinas y maduración del cuello uterino. Mecanísticamente, esto podría relacionarse con la inducción de la menstruación o con la evacuación de tejido retenido.

Ese vínculo no se puede comprobar con los datos disponibles, porque no hay indicaciones originales ni mecanismo de acción registrados. La literatura recuperada trata sobre terminación del embarazo, aborto retenido, sangrado uterino anormal y un caso de hígado graso agudo del embarazo. En esos estudios la amenorrea aparece como criterio de inclusión (embarazo temprano con amenorrea ≤35 días), no como la enfermedad tratada.

El puntaje alto de TxGNN (99.64%) es una predicción del modelo y no equivale a evidencia clínica. Antes de considerar esta dirección habría que precisar qué tipo de amenorrea se quiere tratar (primaria, secundaria o gestacional).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECA | Reprod Sci | Mifepristona en dosis baja con Misoprostol autoadministrado para aborto médico ultratemprano (744 mujeres, amenorrea ≤35 días): evalúa eficacia, seguridad y aceptabilidad |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECA (dosis-respuesta) | Reprod Sci | Dosis bajas de Mifepristona más Misoprostol 200 µg para terminar embarazo ultratemprano (2500 mujeres, amenorrea ≤35 días) |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Estudio clínico | Hum Reprod | Mifepristona en dosis baja con Misoprostol antes de la menstruación esperada para prevenir embarazos no deseados |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Estudio clínico | J Obstet Gynaecol Res | Aborto médico temprano con Mifepristona en dosis baja y Misoprostol autoadministrado |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisión | BMJ | Manejo médico del aborto retenido y del embarazo anembrionario |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisión | J Obstet Gynaecol Can | Ablación endometrial en el sangrado uterino anormal; Misoprostol no es el tema central |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Reporte de caso | Cureus | Hígado graso agudo del embarazo; la amenorrea aparece solo como síntoma de presentación y no guarda relación con Misoprostol |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20189624 | MISO-CARE 200 MCG TABLETA (DKT Colombia S.A.S.) | Tableta (vía oral) | Solo figura "Misoprostol", sin indicación detallada |

El pack informa 8 registros en total, pero los detalles recibidos corresponden a un único número de registro repetido.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como dato adicional, Misoprostol tiene riesgos teratogénicos y uterotónicos conocidos, que son una preocupación para cualquier uso durante el embarazo o el periodo neonatal. No se encontraron interacciones farmacológicas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo: no hay ensayos clínicos y ninguna publicación evalúa Misoprostol para tratar la amenorrea. Además, faltan la indicación original, el mecanismo de acción y los datos de seguridad del prospecto, así que no se puede avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (bloqueante).
- Obtener el mecanismo de acción y la indicación original desde DrugBank.
- Definir qué tipo de amenorrea se busca tratar y buscar estudios específicos.
- Revisión por un especialista en ginecología y endocrinología antes de cualquier decisión.

La segunda predicción del modelo, coartación atípica de la aorta (puntaje 99.30%), no tiene ninguna evidencia y también queda en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

