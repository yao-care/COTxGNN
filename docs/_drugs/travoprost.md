---
layout: default
title: Travoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: De Glaucoma e Hipertensión Ocular a Calcifilaxis Visceral

## Resumen en Una Frase

Travoprost es un agonista tópico del receptor FP de prostaglandinas, usado originalmente para reducir la presión intraocular en glaucoma e hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para **calcifilaxis visceral**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular (el texto del registro sanitario solo dice "TRAVOPROST", sin describir la indicación; esta se toma de los ensayos y del uso conocido del fármaco) |
| Nueva Indicación Predicha | Calcifilaxis visceral |
| Puntaje de Predicción TxGNN | 99.9998% (puntaje saturado, no discrimina entre candidatos) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, travoprost es un agonista del receptor FP de prostaglandinas que se aplica por vía tópica oftálmica. Su eficacia en glaucoma e hipertensión ocular está bien establecida.

Para calcifilaxis visceral **no existe un vínculo mecanístico establecido**. El puntaje del modelo (cercano a 1.0) está saturado y no distingue entre candidatos. No hay ensayos ni literatura que apoyen esta indicación.

Además, la dosificación tópica ocular produce una exposición sistémica mínima. Eso hace poco probable que el fármaco llegue a los tejidos vasculares y viscerales afectados en esta enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los registros de la fuente estaban repetidos; la tabla muestra los dos registros sanitarios distintos (de 20 en total).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20219978 | GLAUCOPROST SOLUCIÓN OFTÁLMICA ESTÉRIL | Solución oftálmica | TRAVOPROST (sin texto de indicación detallado) |
| 19950508 | GLAUCOPROST SOLUCION OFTALMICA | Solución oftálmica | TRAVOPROST (sin texto de indicación detallado) |

Titular de ambos registros: MEGALABS COLOMBIA S.A.S.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo clínico ni bibliográfico (nivel L5) ni un mecanismo plausible para un fármaco tópico ocular. Los demás candidatos revisados (rangos 2 a 10) tampoco tienen evidencia a favor: siete son solo predicción y los otros dos solo aportan evidencia indirecta o de seguridad. Por ejemplo, el reporte de caso de derrame uveal inducido por travoprost en síndrome de Sturge-Weber es una señal de precaución, no de beneficio.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Una hipótesis mecanística explícita que relacione la señalización del receptor FP con la calcifilaxis visceral, con estudios preclínicos que la apoyen
- Datos de exposición sistémica que justifiquen cualquier efecto fuera del ojo
- Advertencias y contraindicaciones del prospecto de INVIMA para completar el análisis de seguridad

*Los resultados son solo para referencia de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

