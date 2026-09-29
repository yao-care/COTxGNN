---
layout: default
title: Glycine
parent: Solo Predicción del Modelo (L5)
nav_order: 212
evidence_level: L5
indication_count: 2
---

# Glycine
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

# Glicina: De Emulsiones Lipidicas a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La glicina es un aminoacido que en Colombia esta registrado como componente de una emulsion inyectable de nutricion parenteral (NUTRIFLEX® OMEGA SPECIAL NOVO, indicacion registrada: "Emulsiones lipidicas").
El modelo TxGNN predice que podria ser efectiva para **enfermedad de la cavidad nasal**, pero la evidencia real es muy debil: **1 ensayo clinico** y **2 publicaciones**, ninguno de los cuales evalua la glicina para esta condicion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Emulsiones lipidicas (nutricion parenteral) |
| Nueva Indicacion Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Prediccion TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Numero de Registros Sanitarios | 20 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion. Segun la informacion conocida, la glicina es parte de una combinacion de aminoacidos, glucosa y lipidos para nutricion parenteral. Su uso en ese contexto es nutricional, y no hay datos que lo relacionen con la enfermedad nasal.

Una hipotesis especulativa es que la glicina tiene efectos antiinflamatorios y citoprotectores, posiblemente a traves de canales de cloruro activados por glicina en celulas inmunes y epiteliales. Esto es solo una idea plausible y no esta respaldada por los datos entregados. No se encontro ningun mecanismo especifico para la cavidad nasal.

El puntaje alto de TxGNN (99.85%) es una prediccion del modelo y no equivale a evidencia clinica. No hay una relacion demostrada entre la indicacion original (nutricion parenteral) y la nueva indicacion.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Fase 1/2 | Completado | 25 | Estudio de imagen PET con el trazador 18F-FPPRGD2 para medir la expresion de integrinas αvβ3 (angiogenesis) en pacientes con glioblastoma, canceres ginecologicos y carcinoma renal. No evalua la glicina ni la enfermedad nasal; no cuenta como evidencia de eficacia. |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinico (formulacion de administracion mucosa) | Chemical & Pharmaceutical Bulletin | Estudia oligoargininas unidas a polimeros como adyuvante mucoso en vacunas nasales en ratones. No trata de glicina. |
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Ciencia basica (histoquimica animal) | Veterinary Pathology | Describe la composicion de glucoconjugados (con lectinas) en mucosa nasal bovina normal e infectada con herpesvirus. No trata de glicina ni de tratamiento. |

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmaceutica | Indicacion Aprobada |
|---------|------|------|-----------|
| 20216947 | NUTRIFLEX® OMEGA SPECIAL NOVO (B. BRAUN MEDICAL S.A.) | Emulsion inyectable | Emulsiones lipidicas |

Nota: el JSON reporta 20 registros en total, pero las cinco entradas disponibles corresponden al mismo registro (20216947), por eso se muestra una sola fila.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se apoya solo en el modelo (L5). El unico ensayo clinico y las dos publicaciones encontradas no estudian la glicina en enfermedad nasal, y no hay un mecanismo verificado que conecte la nutricion parenteral con esta condicion.

**Para avanzar se necesita:**
- Datos del mecanismo de accion (DrugBank) para evaluar un vinculo mecanistico real.
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para el tamizaje de seguridad.
- Estudios preclinicos o clinicos que evaluen la glicina en enfermedad de la cavidad nasal.
- Evaluacion de la compatibilidad de via de administracion: la unica forma registrada es una emulsion inyectable, sin formulacion nasal ni topica.
- La segunda prediccion (laringofaringitis aguda, puntaje 99.84%) tambien tiene nivel L5 y solo un articulo sobre otro farmaco (sivelestat), por lo que tampoco justifica avanzar por ahora.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

