---
layout: default
title: Amoxicillin
parent: Solo Predicción del Modelo (L5)
nav_order: 47
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Amoxicilina: De Antibacteriano Betalactámico a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Amoxicilina es un antibiótico betalactámico de amplio espectro, comercializado en Colombia en combinación con un inhibidor de betalactamasa.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Además, el puntaje alto parece ser un artefacto del grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Amoxicilina y inhibidor de beta-lactamasa (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la amoxicilina es un antibacteriano betalactámico que actúa contra bacterias, y su eficacia en infecciones bacterianas está bien establecida.

Para el síndrome de hiperviscosidad policlonal, que es un exceso de inmunoglobulinas policlonales en sangre que aumenta su viscosidad, **no se identificó ningún mecanismo plausible**. La amoxicilina no tiene efecto conocido sobre la viscosidad sérica ni sobre la producción de inmunoglobulinas. Como tampoco hay datos de indicación original ni de mecanismo de acción, la predicción no puede contrastarse.

El puntaje alto de TxGNN (0.996; posición 3526) parece un artefacto del grafo de conocimiento y no una señal biológica. Otras predicciones tienen el mismo puntaje (por ejemplo, hiperamilasemia), lo que refuerza esta lectura.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20189193 | AMOXIDAL PLUS 600 POLVO PARA RECONSTITUIR A SUSPENSION ORAL (MEGALABS COLOMBIA S.A.S) | Polvo para reconstituir a suspensión oral | Amoxicilina y beta-lactamasa inhibidor |

Nota: el paquete de evidencia reporta 20 registros en total, pero los detalles solo muestran este mismo número de registro repetido, por lo que se presenta una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura para esta indicación, y no se identificó un mecanismo plausible. El puntaje TxGNN alto parece un artefacto del modelo, por lo que no hay base para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Consultar en DrugBank el mecanismo de acción y las indicaciones originales.
- Priorizar otras predicciones del mismo paquete con más respaldo, aunque todavía débil:
  - **Gammapatía monoclonal** (nivel L4, "Research Question"): solo hay reportes de casos sobre la regresión de la enfermedad inmunoproliferativa del intestino delgado tras erradicar *H. pylori*. Esos esquemas no son específicos de amoxicilina.
  - **Peste septicémica** (nivel L4, Hold): hay estudios preclínicos in vitro y en animales, pero faltan datos específicos de amoxicilina y el tratamiento estándar usa otros antibióticos.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

