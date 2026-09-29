---
layout: default
title: Aztreonam
parent: Solo Predicción del Modelo (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: De Antibiótico Monobactámico (indicación no detallada en el registro) a Hiperamilasemia

## Resumen en Una Frase

Aztreonam es un antibiótico monobactámico inyectable que inhibe la proteína de unión a penicilina 3 (PBP3) bacteriana, y en el registro colombiano solo figura con el nombre del principio activo, sin indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Todo indica que se trata de un artefacto del grafo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo repite "AZTREONAM") |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, aztreonam es un monobactámico que inhibe la PBP3 bacteriana, y su uso establecido es antibacteriano contra bacterias gramnegativas. La indicación original tampoco está descrita en los registros.

La hiperamilasemia es un hallazgo de laboratorio no infeccioso. No existe un vínculo mecanístico plausible entre inhibir la PBP3 y normalizar los niveles de amilasa. Además, la polyclonal hyperviscosity syndrome (rank 2) tiene exactamente el mismo puntaje, lo que refuerza la sospecha de un artefacto del grafo de conocimiento sin ancla biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

El Evidence Pack lista el registro 20271484 cuatro veces con datos idénticos, por lo que aquí se muestra una sola vez. Los 8 registros totales no pudieron detallarse individualmente con los datos recibidos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20271484 | Aztreonam 1 g polvo estéril para reconstituir a solución inyectable (Vicarfarmacéutica S.A.) | Polvo estéril para reconstituir a solución inyectable | AZTREONAM (sin detalle de indicación) |
| 20163741 | Azbios® 1 g polvo para reconstituir a solución inyectable (Bioselect S.A.C.I.) | Polvo estéril para reconstituir a solución inyectable | AZTREONAM (sin detalle de indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni literatura para hiperamilasemia, no existe un vínculo mecanístico plausible y el puntaje idéntico al de otra predicción sugiere un artefacto del modelo. No se justifica invertir más recursos en esta indicación.

**Para avanzar se necesita:**
- Descartar formalmente la hiperamilasemia como objetivo de reposicionamiento, salvo que aparezca evidencia independiente.
- Completar el mecanismo de acción desde DrugBank (brecha DG002).
- Obtener advertencias y contraindicaciones del prospecto de INVIMA (brecha DG001, bloqueante para el tamizaje de seguridad).
- Revisar otras predicciones del mismo fármaco con mejor sustento. La más sólida es **uretritis gonocócica** (rank 4, L2, recomendación "Research Question"), respaldada por un ensayo Fase 2/3 completado (NCT03867734, n=32, sitio faríngeo) y varios estudios clínicos de dosis única de 1983-1986. Sus limitaciones son que el ensayo es de un solo brazo y en otro sitio anatómico, que no es aleatorizado y que hay un reporte de gonococos con alta resistencia a cefemas y aztreonam (PMID 11406757).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

