---
layout: default
title: Codeine
parent: Solo Predicción del Modelo (L5)
nav_order: 139
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Codeína: De Combinaciones de Paracetamol (excluyendo psicolépticos) a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La codeína es un opioide que en Colombia se comercializa en combinación con paracetamol, y su registro aparece bajo la categoría "Paracetamol combinaciones excluyendo psicolépticos".
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; es solo una señal del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol combinaciones excluyendo psicolépticos (categoría del registro, no una indicación clínica detallada) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la codeína es un profármaco activado por CYP2D6 que da lugar a morfina y actúa como agonista del receptor opioide µ (gen OPRM1). En Colombia se comercializa en combinación con paracetamol, y su uso clínico establecido es el manejo del dolor. También se usa como antidiarreico y antitusivo.

No se puede verificar un vínculo mecanístico directo con patología nasal. La lista de indicaciones originales está vacía, así que no es posible comparar la indicación original con la nueva. Lo más probable es que la puntuación alta refleje una asociación en el grafo de conocimiento, por ejemplo por síntomas respiratorios compartidos o por cercanía con fármacos antitusivos, y no un efecto terapéutico real.

Entre las otras predicciones del modelo hay una señal que va en sentido contrario al beneficio. Para **urticaria alérgica** (puntaje 99.37%), la literatura muestra que la codeína libera histamina de los mastocitos sin mediación inmunológica y se usa como control positivo en pruebas cutáneas. Además, puede causar urticaria. Ahí la relación es de riesgo, no de tratamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58027 | ALGIMIDE TABLETAS (LABORATORIOS SIEGFRIED S.A.S.) | Tableta | Paracetamol combinaciones excluyendo psicolépticos |

Los cinco registros recibidos corresponden al mismo número sanitario y producto, por lo que se muestran una sola vez. El paquete indica 20 registros en total, pero no se recibió el detalle de los demás.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la única entrada disponible es farmacológica, no una interacción con otro medicamento. Muestra que la codeína actúa sobre el receptor µ opioide (OPRM1, humano). No se dispone de interacciones fármaco-fármaco con nivel de gravedad.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para enfermedad de la cavidad nasal tiene un puntaje muy alto (99.93%), pero es solo una predicción del modelo (L5), sin ensayos ni publicaciones. No existe un vínculo mecanístico verificable, y de las otras predicciones, la de urticaria es mecanísticamente contraria a un uso terapéutico.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), requisito previo al tamizaje de seguridad.
- Obtener el mecanismo de acción desde DrugBank para evaluar un posible vínculo con patología nasal.
- Una búsqueda dirigida de estudios sobre codeína en enfermedad nasal, para confirmar si la señal es un artefacto del grafo.
- Aclarar la indicación original detallada de los productos con codeína registrados (20 registros, solo se recibió uno).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

