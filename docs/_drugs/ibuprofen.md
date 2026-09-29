---
layout: default
title: Ibuprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 218
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Ibuprofeno: De Analgésico y Antipirético a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Ibuprofeno es un antiinflamatorio no esteroideo (AINE) de uso amplio como analgésico y antipirético, comercializado en Colombia, entre otras presentaciones, como suspensión oral pediátrica.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, una displasia esquelética rara, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ibuprofeno (el texto del registro INVIMA solo indica el nombre del principio activo; el uso clínico conocido es analgésico y antipirético) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Los datos farmacológicos disponibles indican que ibuprofeno actúa sobre COX-1 y COX-2, es decir, es un inhibidor no selectivo de la ciclooxigenasa. También aparecen como dianas PPAR-γ, ASIC1, SMCT1 y el transportador de aminoácidos acoplado a protones 1 (PAT1). Su eficacia como analgésico y antipirético está bien establecida.

**No se ha podido establecer un vínculo mecanístico** entre esta acción y la displasia acromesomélica tipo Hunter-Thompson. Esta enfermedad es una displasia esquelética rara que probablemente se origina en un defecto de señalización de factores de crecimiento (vía GDF5, no verificada en los datos suministrados). No es un proceso mediado por COX ni una condición inflamatoria. La indicación original (dolor y fiebre) y la nueva indicación no tienen similitud clínica ni fisiopatológica demostrada.

El puntaje de 0.997 (posición 2747 en el ranking del modelo) refleja solo cercanía en el grafo de conocimiento. Por sí solo no justifica avanzar sin evidencia adicional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 227672 | ADVIL® CHILDREN SUSPENSION ORAL PARA NIÑOS (HALEON COLOMBIA S.A.S) | Suspensión oral | IBUPROFENO (el registro no detalla la indicación) |

Se reportan 20 registros sanitarios en total. Los 5 registros incluidos en el paquete de evidencia son entradas repetidas del mismo número (227672), por lo que se muestran una sola vez. La única vía de administración documentada es la oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo TxGNN (nivel de evidencia L5), sin ensayos clínicos, sin literatura y sin un mecanismo plausible que conecte la inhibición de COX con una displasia esquelética de origen genético. Las otras seis predicciones del ranking (síndrome braquiolmia-amelogénesis imperfecta, miosclerosis, braquiolmia, síndrome braquidactilia-sindactilia, pseudoacondroplasia y síndrome de microftalmia colobomatosa-displasia rizomélica) tienen el mismo nivel de evidencia y la misma recomendación.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción completo desde DrugBank.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para el cribado de seguridad.
- Hacer una búsqueda sistemática en PubMed y ClinicalTrials.gov, con y sin nombre del fármaco, sobre la vía GDF5/BMP y el uso de AINE en esta displasia.
- Confirmar la fisiopatología de la enfermedad con fuentes independientes.
- Si hay evidencia mecanística, evaluar estudios preclínicos antes de considerar estudios clínicos. Un posible beneficio sintomático (dolor articular) no constituye una indicación de reposicionamiento.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

