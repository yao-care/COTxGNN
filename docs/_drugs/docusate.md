---
layout: default
title: Docusate
parent: Solo Predicción del Modelo (L5)
nav_order: 229
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Docusate: nueva indicación predicha, Síndrome de Plummer-Vinson (nivel de evidencia L5). Indicación original: Sodio docusato"
monitor_inn: "docusate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
---

# Docusate
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

## Docusato: De Ablandador de Heces (Docusato Sódico) a Síndrome de Plummer-Vinson
{: .text-alpha }

## Resumen en Una Frase

El docusato es un tensioactivo aniónico utilizado como ablandador de heces; en Colombia su registro sanitario figura con la indicación "Sodio docusato".
El modelo TxGNN predice que podría ser efectivo para el **síndrome de Plummer-Vinson**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sodio docusato (texto de indicación del registro INVIMA; no detalla una enfermedad específica) |
| Nueva Indicación Predicha | Síndrome de Plummer-Vinson |
| Puntaje de Predicción TxGNN | 0.9918 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el docusato es un tensioactivo aniónico que permite que el agua y las grasas penetren en las heces, y su uso establecido es como ablandador fecal. No existe evidencia en los datos compilados de que este mecanismo sea aplicable al síndrome de Plummer-Vinson.

El síndrome de Plummer-Vinson se caracteriza por anemia ferropénica, membranas esofágicas y disfagia, y se trata con reposición de hierro y dilatación esofágica. El docusato no tiene un papel conocido en la absorción de hierro ni en la fisiopatología de las membranas esofágicas. La relación entre la indicación original (estreñimiento) y la nueva indicación es, por tanto, muy débil.

Una hipótesis puramente especulativa sería que la actividad tensioactiva modifica las propiedades de la mucosa, pero no tiene respaldo en los datos. El puntaje alto de TxGNN (0.9918) es solo una predicción del modelo de aprendizaje profundo, que puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, sin evidencia mecanística ni clínica.

Cabe mencionar una segunda predicción del modelo: la **anemia megaloblástica constitucional independiente de vitamina B12 y folato** (puntaje 0.9915). Tampoco cuenta con ensayos ni literatura, y el docusato no tiene efecto reconocido sobre las vías de síntesis de nucleótidos implicadas.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19913206 | SENNAX PLUS® TABLETAS RECUBIERTAS | Tableta recubierta | SODIO DOCUSATO | Vigente |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** enfermedad ulcerosa péptica, deficiencia de potasio, anemia de células falciformes, persistencia hereditaria de hemoglobina fetal, hiperoxaluria primaria, hemocromatosis hereditaria, hemosiderosis, trastornos del metabolismo del hierro, enfermedad de Wilson, colitis ulcerosa, enfermedad inflamatoria intestinal, anemia hemolítica, apendicitis, gastritis atrófica crónica, neuropatía óptica hereditaria de Leber y gastroenteritis.
  - Es relevante que varias de estas condiciones (trastornos del metabolismo del hierro, anemia hemolítica) están relacionadas con las anemias de las indicaciones predichas.
- **Interacciones Farmacológicas** (4 registradas):

| Fármaco Interactuante | Nivel |
|------|------|
| Lactulosa | Moderado |
| Mineral oil (aceite mineral) | Moderado |
| Fenolftaleína | Moderado |
| Linaclotida | Menor |

Consultar el prospecto para información adicional de advertencias y contraindicaciones, ya que no se dispone de ella en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos clínicos ni literatura, sin vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-docusate-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos clínicos ni literatura, sin vínculo mecanístico plausible y con el único registro sanitario colombiano cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-docusate-1 -->

**Para avanzar se necesita:**
- Obtener el mecanismo de acción del docusato desde DrugBank y evaluar si existe algún vínculo biológico con el síndrome de Plummer-Vinson.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Realizar una revisión de literatura y de registros de ensayos clínicos que confirme la ausencia o presencia de estudios.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original (actualmente pendientes).

<!-- review:begin co-lic-20261105-docusate-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la compatibilidad de vías de administración y la similitud con la indicación original (actualmente pendientes). / Considerar que el fármaco no tiene registros vigentes en Colombia, lo que implicaría un nuevo trámite regulatorio." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-docusate-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y con el único registro sanitario colombiano cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Considerar que el fármaco no tiene registros vigentes en Colombia, lo que implicaría un nuevo trámite regulatorio" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

