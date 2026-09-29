---
layout: default
title: Clofazimine
parent: Solo Predicción del Modelo (L5)
nav_order: 134
evidence_level: L5
indication_count: 3
---

# Clofazimine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Clofazimina: De Lepra a Neumocistosis

## Resumen en Una Frase

Clofazimina es un antimicobacteriano utilizado originalmente, dentro de la terapia multifarmaco, para tratar la lepra.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**,
pero solo hay **1 ensayo clínico** con relevancia baja (sobre otra infección, no sobre *Pneumocystis*) y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo indica "CLOFAZIMINA" (sin detalle de indicación). Según la literatura farmacológica: lepra, en combinación con otros antibacterianos |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, clofazimina es parte de los esquemas de terapia multifármaco contra la lepra (junto con rifampicina y dapsona) y se usa también en tuberculosis resistente. Su actividad comprobada es contra micobacterias.

Hasta ahora no existe un mecanismo establecido que vincule a clofazimina con actividad contra *Pneumocystis*. El único ensayo asociado estudia la prevención de la infección por *Mycobacterium avium* en personas con VIH. En esa población *Pneumocystis* es una coinfección frecuente, pero el ensayo no evaluó el efecto del fármaco sobre este hongo.

El puntaje alto de TxGNN (99.90%) proviene únicamente del grafo de conocimiento y no de estudios reales. Por eso esta predicción debe considerarse una hipótesis sin respaldo experimental.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | Fase NA | Completado | No reportada | Estudio aleatorizado de profilaxis con clofazimina para prevenir la infección por *Mycobacterium avium* en personas con VIH. Relevancia baja (grado C): no evalúa *Pneumocystis* ni aporta señal directa de eficacia o seguridad para neumocistosis |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20274960 | CLOFZIMIN® 100 MG (VESALIUS PHARMA S.A.S.) | Tableta recubierta | CLOFAZIMINA (sin detalle de indicación en el registro) |

El paquete de datos contiene 5 entradas idénticas del mismo registro, por lo que se muestra una sola fila. Vía de administración: oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5). No hay mecanismo plausible, literatura ni ensayos que evalúen clofazimina contra *Pneumocystis*. El único ensayo vinculado trata otra infección oportunista.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de clofazimina (DrugBank) y análisis de su posible relación con *Pneumocystis*.
- Estudios *in vitro* e *in vivo* de actividad anti-*Pneumocystis*, que hoy no existen.
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad.
- Aclarar la indicación aprobada en el registro sanitario colombiano, que solo dice "CLOFAZIMINA".
- Como referencia, la segunda predicción (malaria, nivel L4) tiene un estudio *in vitro* sobre análogos de clofazimina. Esa línea es preclínica, pero está mejor respaldada que la de neumocistosis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

