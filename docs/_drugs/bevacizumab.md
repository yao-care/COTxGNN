---
layout: default
title: Bevacizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: De Indicación Original No Documentada a Neoplasia de Epiglotis

## Resumen en Una Frase

Bevacizumab es un anticuerpo monoclonal que se comercializa en Colombia, pero los datos recibidos no indican para qué se aprobó originalmente.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de epiglotis**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible. El registro sanitario solo repite el nombre del principio activo ("BEVACIZUMAB"), sin texto de indicación. |
| Nueva Indicación Predicha | Neoplasia de epiglotis |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según el conocimiento general (no proviene de los datos recibidos), bevacizumab bloquea el factor de crecimiento endotelial vascular (VEGF) y así limita la formación de nuevos vasos sanguíneos que alimentan a los tumores.

El modelo plantea que esta actividad anti-VEGF podría ser útil en tumores de cabeza y cuello que dependen de la angiogénesis, como los de la epiglotis. Es una hipótesis plausible, pero el paquete no contiene ningún ensayo ni publicación que la respalde para este sitio anatómico. Tampoco hay información sobre la indicación original, por lo que no se puede analizar la similitud entre ambas.

La predicción se apoya solo en el puntaje del modelo (99.90%, posición 1249 en el ranking TxGNN). Debe tratarse como una hipótesis por verificar.

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
| 20255030 | BEVASTIM ® (Laboratorios Legrand S.A.) | Solución concentrada para infusión | No especificada (solo figura "BEVACIZUMAB") |

Los datos listan 5 filas idénticas del mismo registro 20255030; aquí se muestran una sola vez. El total informado es de 20 registros sanitarios, pero solo se recibió el detalle de este.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-VEGF), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto. Como referencia general: presión arterial, proteinuria y hemograma |
| Protección en Manejo | Seguir el protocolo institucional para medicamentos oncológicos parenterales |

Estos datos no vienen del paquete de evidencia. La clasificación se deduce de la naturaleza del fármaco.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia de epiglotis es solo del modelo (nivel L5), sin ensayos clínicos ni literatura, y no se conoce la indicación original ni los datos de seguridad locales. No hay base para avanzar todavía.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, que es un vacío bloqueante para el tamizaje de seguridad.
- Consultar DrugBank para obtener el mecanismo de acción y las indicaciones originales.
- Hacer una búsqueda dirigida de ensayos y literatura sobre bevacizumab en tumores de laringe y epiglotis.
- Definir si la neoplasia de epiglotis es maligna o benigna en el mapeo de enfermedades, porque de eso depende la relevancia clínica.
- Revisar la predicción "cystic neoplasm" (posición 7), que sí tiene evidencia L1 en cáncer de ovario. Es probable que ese uso ya esté establecido y no sea reposicionamiento nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

