---
layout: default
title: Dexchlorpheniramine
parent: Solo Predicción del Modelo (L5)
nav_order: 159
evidence_level: L5
indication_count: 2
---

# Dexchlorpheniramine
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

# Dexclorfeniramina: De Combinaciones de Paracetamol (excluyendo psicolépticos) a Urticaria Alérgica

## Resumen en Una Frase

Dexclorfeniramina es un antihistamínico H1 de primera generación. En Colombia se comercializa dentro de una combinación pediátrica con acetaminofén (paracetamol).
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, pero hoy no hay **ningún ensayo clínico** registrado. Solo hay **6 publicaciones**, casi todas de farmacodinamia o indirectas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones de paracetamol excluyendo psicolépticos (texto de clasificación, no una indicación clínica detallada) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 (débil: estudios farmacodinámicos e indirectos, sin ensayos en pacientes con urticaria) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, la dexclorfeniramina es un antagonista del receptor H1 de primera generación. En Colombia se usa en una combinación pediátrica con acetaminofén, y mecanísticamente podría ser aplicable a la urticaria alérgica.

En la urticaria alérgica, la histamina liberada por los mastocitos produce ronchas, eritema y prurito. Bloquear el receptor H1 ataca ese mecanismo de forma directa, y por eso el puntaje alto de TxGNN es biológicamente plausible. Esta explicación se basa en la clase del fármaco y no en datos del registro.

La indicación original registrada (combinaciones de paracetamol) no guarda una relación directa con la urticaria. La predicción se apoya en el efecto antihistamínico del componente, no en la indicación de la combinación comercial.

La segunda predicción del modelo, **urticaria por frío** (puntaje 99.61%), tiene la misma lógica de clase. No tiene ensayos ni literatura, así que es solo una predicción (nivel L5, Hold).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Ensayo aleatorizado fase I (farmacodinámico) | Eur J Pharm Sci | Compara bilastina oral, dexclorfeniramina parenteral y una nueva bilastina parenteral en la inhibición de la roncha y el eritema inducidos por histamina. El resumen disponible está truncado y no incluye resultados. |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Estudio farmacodinámico comparativo | An Bras Dermatol | Compara la supresión de roncha y eritema por los principales antihistamínicos H1 comercializados en Brasil. |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Reporte de caso | Dermatologica | Urticaria por contacto con calor en una mujer joven. El papel de la dexclorfeniramina no es claro. |
| [28601540](https://pubmed.ncbi.nlm.nih.gov/28601540/) | 2017 | Reporte clínico / revisión | Am J Med | Fibrilación auricular en anafilaxia. La dexclorfeniramina aparece probablemente como cotratamiento, por lo que la relevancia es indirecta. |
| [26179134](https://pubmed.ncbi.nlm.nih.gov/26179134/) | 2015 | Reporte de caso | Contact Dermatitis | Angioedema palpebral y dermatitis de contacto alérgica por un cerumenolítico. Relevancia indirecta. |
| [2523357](https://pubmed.ncbi.nlm.nih.gov/2523357/) | 1989 | Estudio in vitro / ex vivo | Int Arch Allergy Appl Immunol | Inhibición de la quimiotaxis de eosinófilos por cetirizina. Es mecanístico y no evalúa dexclorfeniramina directamente. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50400 | CORICIDIN® GOTAS PEDIÁTRICAS CON ACETAMINOFEN (Bayer S.A.) | Solución oral | Paracetamol combinaciones excluyendo psicolépticos |

El registro reporta 6 licencias, pero el listado contiene entradas repetidas del mismo registro 50400, por lo que solo se muestra una fila.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo H1 es plausible y el puntaje del modelo es alto. Sin embargo, la evidencia se limita a estudios farmacodinámicos de roncha y eritema y a reportes indirectos, sin ensayos clínicos en pacientes con urticaria. Además, no se cuenta con las advertencias ni las contraindicaciones del prospecto de INVIMA, lo que bloquea la evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que hoy es el vacío bloqueante.
- Confirmar el mecanismo de acción en DrugBank.
- Revisar el texto completo del estudio 39265704 y buscar ensayos clínicos en urticaria con dexclorfeniramina como fármaco de estudio.
- Evaluar la compatibilidad de vía: el producto colombiano es una solución oral pediátrica en combinación con acetaminofén, mientras que la evidencia farmacodinámica usó la vía parenteral.
- Considerar el perfil sedante propio de los antihistamínicos de primera generación, señalado en la literatura, dentro de un plan de monitoreo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

