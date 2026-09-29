---
layout: default
title: Esomeprazole
parent: Evidencia Moderada (L3-L4)
nav_order: 184
evidence_level: L4
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Esomeprazol: De Trastornos Ácido-Pépticos a Reflujo Duodenogástrico

## Resumen en Una Frase

Esomeprazol es un inhibidor de la bomba de protones que se usa para reducir la producción de ácido en el estómago, en enfermedades como el reflujo gastroesofágico y las úlceras.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico** (reflujo de bilis hacia el estómago), pero la evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** (una revisión general sobre inhibidores de la bomba de protones).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en el registro (el texto registrado es solo "Esomeprazol"); la farmacología lo describe como antiácido para reflujo gastroesofágico y exceso de ácido gástrico |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información farmacológica, esomeprazol actúa sobre ATP4A, la bomba H+/K+-ATPasa del estómago, y reduce la producción de ácido. Su eficacia en enfermedades relacionadas con el ácido gástrico está bien establecida.

El reflujo duodenogástrico se debe a fallas en el píloro y en la motilidad, no a un exceso de ácido. Por eso, reducir el ácido podría aliviar síntomas de gastritis o esofagitis asociadas al reflujo, pero **no corrige el reflujo en sí**. El vínculo mecanístico es, por tanto, indirecto y débil.

El puntaje TxGNN es muy alto (0.995), pero probablemente refleja la cercanía en el grafo de conocimiento con trastornos gastrointestinales relacionados con el ácido, y no un mecanismo específico. La única fuente de apoyo es una revisión general sobre inhibidores de la bomba de protones, no un estudio de esta condición.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | Eur J Clin Pharmacol | Actualización del uso clínico y la farmacocinética de los inhibidores de la bomba de protones, fármacos de primera elección en úlcera péptica, infección por *H. pylori*, reflujo gastroesofágico, lesiones por AINE y síndrome de Zollinger-Ellison. No aborda el reflujo duodenogástrico. |

## Información de Mercado en Colombia

Se registran 20 registros sanitarios en total. Los cinco primeros listados en los datos corresponden al mismo registro, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155892 | ACIDPRAZOL® 40 MG CÁPSULA | Cápsula dura | Esomeprazol (sin detalle de indicación) |

Otras formas farmacéuticas disponibles en Colombia: tableta con recubrimiento entérico (vía oral).

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones medicamentosas registradas. El único registro es farmacológico: el objetivo ATP4A (bomba H+/K+-ATPasa gástrica humana).

Consultar el prospecto para información de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Solo existe una revisión general de inhibidores de la bomba de protones y ningún ensayo clínico para reflujo duodenogástrico. El mecanismo (supresión de ácido) no corrige la causa del reflujo biliar, y el puntaje TxGNN probablemente refleja cercanía en el grafo y no eficacia.

**Para avanzar se necesita:**
- Estudios clínicos u observacionales específicos de esomeprazol en reflujo duodenogástrico o gastritis por reflujo biliar.
- Datos del mecanismo de acción y del prospecto de INVIMA (advertencias y contraindicaciones).
- Verificar la indicación original registrada, ya que el texto actual solo dice "Esomeprazol".
- Como nota aparte: la predicción de rango 3, **úlcera duodenal**, tiene evidencia mucho más sólida (nivel L1, con varios ensayos de Fase 3 completados). Probablemente corresponde a un uso ya autorizado y no a un reposicionamiento real, así que conviene evaluarla por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

