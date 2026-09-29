---
layout: default
title: Cabergoline
parent: Evidencia Moderada (L3-L4)
nav_order: 105
evidence_level: L4
indication_count: 5
---

# Cabergoline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Cabergolina: De Hiperprolactinemia a Adenocarcinoma Hipofisario

## Resumen en Una Frase

La cabergolina es un agonista dopaminérgico D2 usado originalmente para tratar trastornos hiperprolactinémicos y los síntomas de la enfermedad de Parkinson.
El modelo TxGNN predice que podría ser efectiva para **adenocarcinoma hipofisario**,
pero hoy hay **0 ensayos clínicos** y solo **3 publicaciones** (todas reportes de caso, de relevancia indirecta) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastornos hiperprolactinémicos y enfermedad de Parkinson (el texto del registro INVIMA solo dice "CABERGOLINA"; la indicación proviene de la información farmacológica del fármaco) |
| Nueva Indicación Predicha | Adenocarcinoma hipofisario |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La cabergolina es un agonista de los receptores de dopamina D2. Estos receptores se expresan en muchos tumores hipofisarios, lo que ofrece una base biológica para la predicción. Su perfil farmacológico también incluye actividad sobre receptores de serotonina (5-HT), adrenérgicos y otros subtipos de dopamina (D1 a D5). Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco.

La hiperprolactinemia suele originarse en un adenoma hipofisario (prolactinoma), y la cabergolina ya se usa para reducir la secreción hormonal y el tamaño de estos tumores. De ahí que el modelo extienda la asociación a otros tumores de la hipófisis. El adenocarcinoma hipofisario es, sin embargo, una entidad mucho más rara y agresiva que el adenoma.

La evidencia recuperada no confirma esa extensión. Incluye un reporte de caso sobre hipersecreción ectópica de corticotropina tratada con octreótido o cabergolina, un reporte no relacionado de adenocarcinoma pancreático y un caso de neoplasia endocrina múltiple con una variante génica de significado incierto. Ninguno muestra beneficio en carcinoma hipofisario. El puntaje alto de TxGNN es una predicción basada en grafos, no una confirmación clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Reporte de caso | Endocr Pract | Respuesta de la corticotropina al tratamiento prolongado con octreótido o cabergolina en una paciente con secreción ectópica de corticotropina tras adrenalectomía. Es la única publicación de relevancia indirecta. |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Reporte de caso | Rev Esp Enferm Dig | Linfangiectasias duodenales como primer signo de adenocarcinoma pancreático en una paciente con adenoma hipofisario tratada con cabergolina. No guarda relación con carcinoma hipofisario. |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Reporte de caso | Medicine | Neoplasia endocrina múltiple con curso clínico atípico y una variante del gen MEN1 de patogenicidad incierta. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20097607 | CABERGOLINA 0.5 MG (Laboratorios MK S.A.S.) | Tableta | CABERGOLINA (el texto solo repite el nombre del principio activo) |

Nota: los cinco registros listados en los datos corresponden al mismo número sanitario (20097607) y se muestran una sola vez. El total reportado es de 20 registros. La única vía de administración disponible es la oral.

## Consideraciones de Seguridad

- **Perfil de receptores**: la cabergolina actúa sobre receptores dopaminérgicos (D1 a D5), serotoninérgicos (5-HT1A, 1B, 1D, 2A, 2B, 2C) y adrenérgicos (α1A, α2A, α2B, α2C). Los datos no incluyen interacciones fármaco-fármaco con nivel de gravedad.
- **Señales de seguridad en la literatura recuperada** (de otras indicaciones evaluadas):
  - Valvulopatía cardíaca con uso prolongado o a dosis altas. Es un tema debatido y la mayoría de los estudios no encuentra un riesgo significativo.
  - Trastornos del control de impulsos.
  - Glaucoma de ángulo cerrado bilateral (reporte de caso).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es biológicamente plausible por la vía D2, pero no hay ensayos clínicos y la literatura es solo de reportes de caso sin beneficio demostrado en carcinoma hipofisario. La evidencia clínica sólida de cabergolina está en adenomas hipofisarios, no en carcinoma.

Cabe señalar que la predicción vecina "cáncer de hipófisis" (rango 3) tiene mucho más respaldo: L2, con ensayos de Fase 3 en adenomas (NCT03271918, NCT00889525, NCT07463235) y una decisión de "Proceed with Guardrails". Esa evidencia es de adenoma, no de carcinoma, y conviene evaluarla por separado.

**Para avanzar se necesita:**
- Búsqueda dirigida de evidencia específica en carcinoma hipofisario (series de casos, estudios observacionales, ensayos)
- Datos detallados del mecanismo de acción y análisis de relación con la indicación original
- Prospecto INVIMA con advertencias y contraindicaciones oficiales
- Plan de seguridad: monitoreo de valvulopatía cardíaca, límites de dosis y supervisión endocrinológica

Los resultados de este informe son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

