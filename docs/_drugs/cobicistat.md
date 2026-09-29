---
layout: default
title: Cobicistat
parent: Solo Predicción del Modelo (L5)
nav_order: 138
evidence_level: L5
indication_count: 3
---

# Cobicistat
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

# Cobicistat: De Combinación Darunavir/Cobicistat a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Cobicistat se comercializa en Colombia dentro de la combinación darunavir/cobicistat (PREZCOBIX®). El registro sanitario no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que por ahora es solo una señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Darunavir y cobicistat (el registro solo indica la combinación, sin describir la indicación) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información del análisis, cobicistat es un inhibidor de CYP3A basado en mecanismo y funciona como potenciador farmacocinético. No tiene actividad antiviral propia. En los esquemas contra el VIH-1 aumenta la exposición a otros antirretrovirales, como darunavir, atazanavir o elvitegravir.

La única razón para plantear la nueva indicación es una analogía. El virus de inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH-1. Sin embargo, su proteasa y su integrasa son distintas a las del VIH-1. No se ha demostrado que un esquema potenciado funcione en gatos, y la farmacología de CYP3A en felinos no está caracterizada. El puntaje alto (0.999) probablemente refleja cercanía en el grafo de conocimiento con nodos relacionados con el VIH, y no evidencia independiente.

TxGNN generó otras dos predicciones con el mismo tipo de limitaciones, ambas de nivel L5 y con decisión Hold:
- **Infección por virus de inmunodeficiencia simia** (puntaje 99.92%, idéntico al felino, lo que sugiere que ambas provienen del mismo vecindario del grafo). Cobicistat solo podría servir como potenciador de otros antirretrovirales en un modelo de macacos, por lo que por sí solo no aporta evidencia de eficacia.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical** (puntaje 99.91%). No se identificó ningún vínculo mecanístico plausible. Es probable que sea un artefacto del grafo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los cinco registros detallados en los datos corresponden al mismo número de registro sanitario, por lo que se presentan una sola vez. El total reportado es de 8 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20104155 | PREZCOBIX® TABLETAS RECUBIERTAS (JANSSEN CILAG S.A.) | Tableta recubierta | Darunavir y cobicistat |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres predicciones son de nivel L5, sin ensayos ni literatura, y cobicistat no tiene actividad antiviral propia. El puntaje alto parece reflejar la estructura del grafo y no eficacia. La indicación felina además corresponde a medicina veterinaria, lo que exige un marco regulatorio distinto al de un registro humano.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones, que hoy es un vacío bloqueante para el tamizaje de seguridad.
- Estudios preclínicos que muestren un beneficio farmacocinético de cobicistat en gatos, junto con un antirretroviral activo contra FIV.
- Confirmar si esta línea tiene sentido dentro del alcance de reposicionamiento en humanos, ya que las tres predicciones son veterinarias o sin vínculo mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

