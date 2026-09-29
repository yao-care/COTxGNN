---
layout: default
title: Acyclovir
parent: Solo Predicción del Modelo (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Acyclovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Aciclovir: De Infecciones por Herpesvirus a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Aciclovir es un antiviral que en Colombia se comercializa con 20 registros sanitarios, entre ellos un ungüento tópico y una tableta recubierta oral. Su uso conocido es contra virus herpes (HSV/VZV), aunque el texto de indicación de los registros solo indica el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**, con **0 ensayos clínicos** y **2 publicaciones** que no evalúan aciclovir, por lo que no hay respaldo real para esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ACICLOVIR (el registro solo indica el principio activo, sin texto de indicación) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, aciclovir se activa mediante la timidina cinasa viral del HSV y del VZV, y por eso es eficaz contra las infecciones por esos herpesvirus.

La queratitis epitelial punteada suele ser de origen adenoviral y, con menos frecuencia, herpético o microsporidial. Solo la causa herpética se relaciona con el mecanismo de aciclovir. Los adenovirus y los microsporidios no dependen de esa timidina cinasa, así que no se espera un efecto antiviral relevante en ellos.

El puntaje alto de TxGNN (0.997) es una predicción basada en el grafo de conocimiento y no tiene respaldo clínico. Ninguno de los dos artículos recuperados prueba aciclovir en esta condición.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Serie de casos | American Journal of Ophthalmology | Dos pacientes con SIDA desarrollaron lipidosis corneal por fármacos que se unen a fosfolípidos lisosomales. No evalúa aciclovir. |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Serie de casos | Indian Journal of Pathology & Microbiology | Características de la queratoconjuntivitis microsporidial en una cohorte del este de la India. No evalúa aciclovir. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 219368 | VIREX® UNGÜENTO (EUROFARMA COLOMBIA S.A.S.) | Ungüento tópico | ACICLOVIR (solo el nombre del principio activo) |

El paquete de evidencia repite este mismo registro cinco veces, por lo que se muestra una sola vez. Además del ungüento tópico, el farmaco tiene autorizada la tableta recubierta por vía oral. Ninguna de las formas listadas es oftálmica, y la compatibilidad de vía para esta indicación no ha sido evaluada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos y la literatura recuperada no prueba aciclovir. Además, la causa más frecuente (adenovirus) no es susceptible al mecanismo del fármaco.

**Para avanzar se necesita:**
- Definir el agente causal. Solo la queratitis epitelial herpética tendría un vínculo mecanístico plausible con aciclovir.
- Una búsqueda dirigida de literatura sobre aciclovir en queratitis herpética epitelial.
- Datos de seguridad del prospecto de INVIMA y evaluación de una formulación oftálmica, ya que las formas registradas son tópica cutánea y oral.
- Como referencia, entre las otras predicciones de este fármaco, **verruga común** tiene la evidencia más sólida (nivel L2, seis ensayos, cuatro de ellos comparaciones aleatorizadas de aciclovir intralesional). Conviene evaluarla en un informe aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

